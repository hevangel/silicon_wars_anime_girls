import http from 'node:http';
import { createReadStream } from 'node:fs';
import { readFile, realpath, stat } from 'node:fs/promises';
import { execFile } from 'node:child_process';
import { promisify } from 'node:util';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { root, upstream, loadCatalog } from './catalog.mjs';
import { JobManager, codexBinary } from './jobs.mjs';

const appRoot = fileURLToPath(new URL('../', import.meta.url));
const port = Number(process.env.PORT || 5200);
if (!Number.isInteger(port) || port < 1024 || port > 65535) throw Error('PORT must be 1024–65535.');
const origin = `http://127.0.0.1:${port}`;
const catalog = await loadCatalog(origin);
const jobs = new JobManager(catalog, origin);
const development = process.argv.includes('--dev');
const vite = development ? await (await import('vite')).createServer({root: appRoot, server: {middlewareMode: true}, appType: 'spa'}) : null;
const mime = {'.png':'image/png','.jpg':'image/jpeg','.jpeg':'image/jpeg','.webp':'image/webp','.svg':'image/svg+xml','.ico':'image/x-icon','.json':'application/json','.js':'text/javascript','.css':'text/css','.html':'text/html','.md':'text/plain','.txt':'text/plain'};
const json = (res, status, data) => { res.writeHead(status, {'Content-Type':'application/json','Cache-Control':'no-store','X-Content-Type-Options':'nosniff'}); res.end(JSON.stringify(data)); };

async function serve(res, base, relative) {
  const file = path.resolve(base, relative);
  const actualBase = await realpath(base);
  const actual = await realpath(file);
  if (!actual.startsWith(`${actualBase}${path.sep}`)) throw Object.assign(Error('Forbidden'), {status: 403});
  const info = await stat(actual);
  if (!info.isFile()) throw Object.assign(Error('Not found'), {status:404});
  res.writeHead(200, {'Content-Type':mime[path.extname(actual)] || 'application/octet-stream', 'Content-Length':info.size,'X-Content-Type-Options':'nosniff'});
  createReadStream(actual).pipe(res);
}

const server = http.createServer(async (req, res) => {
  try {
    // Bind and validate loopback Host, Origin and Fetch Metadata before allowing CLI execution.
    if (req.headers.host !== `127.0.0.1:${port}`) return json(res, 403, {error:'Use the printed 127.0.0.1 URL.'});
    if ((req.headers.origin && req.headers.origin !== origin) || req.headers['sec-fetch-site'] === 'cross-site') return json(res,403,{error:'Cross-origin requests are disabled.'});
    const url = new URL(req.url, origin);
    const pathname = decodeURIComponent(url.pathname);
    if (pathname === '/api/catalog' && req.method === 'GET') return json(res,200,catalog);
    if (pathname === '/api/health' && req.method === 'GET') {
      try { const {stdout} = await promisify(execFile)(codexBinary, ['--version'], {windowsHide:true, timeout:5000}); return json(res,200,{ready:true,version:stdout.trim(),imageGeneration:'Requires an image tool in the local Codex session.'}); }
      catch (error) { return json(res,200,{ready:false,error:error.code === 'EPERM' || error.code === 'EACCES' ? 'The server lacks permission to launch Codex CLI.' : 'Codex CLI is unavailable. Check installation, sign-in and CODEX_BIN.'}); }
    }
    if (pathname === '/api/jobs' && req.method === 'POST') {
      if (!req.headers['content-type']?.startsWith('multipart/form-data')) return json(res,415,{error:'Expected multipart form data.'});
      const chunks = []; let size = 0;
      for await (const chunk of req) { size += chunk.length; if (size > 32*1024*1024) return json(res,413,{error:'Request too large.'}); chunks.push(chunk); }
      const form = await new Request(`${origin}/api/jobs`, {method:'POST', headers:{'Content-Type':req.headers['content-type']}, body:Buffer.concat(chunks)}).formData();
      let references;
      try { references = JSON.parse(form.get('references')); } catch { return json(res,400,{error:'Invalid references.'}); }
      if (Array.isArray(references)) for (const reference of references) {
        if (!reference.upload) continue;
        if (reference.kind !== 'costume') return json(res,400,{error:'Characters must come from the Silicon Wars roster.'});
        const file = form.get(reference.upload);
        if (!file || typeof file.arrayBuffer !== 'function' || file.size > 10*1024*1024 || !['image/png','image/jpeg','image/webp'].includes(file.type)) return json(res,400,{error:'Costume upload must be PNG, JPEG or WebP, up to 10 MB.'});
        const bytes = Buffer.from(await file.arrayBuffer());
        const valid = file.type === 'image/png' ? bytes.subarray(0,8).equals(Buffer.from([137,80,78,71,13,10,26,10])) : file.type === 'image/jpeg' ? bytes.subarray(0,3).equals(Buffer.from([255,216,255])) : bytes.toString('ascii',0,4) === 'RIFF' && bytes.toString('ascii',8,12) === 'WEBP';
        if (!valid) return json(res,400,{error:'Invalid costume image.'});
        reference.uploadData = bytes; reference.extension = {'image/png':'.png','image/jpeg':'.jpg','image/webp':'.webp'}[file.type];
      }
      const submitted = await jobs.submit({prompt:form.get('prompt'),size:form.get('size'),quality:form.get('quality'),mode:form.get('mode'),references});
      return json(res,202,submitted);
    }
    const match = /^\/api\/jobs\/([\w-]+)$/.exec(pathname);
    if (match) {
      const job = jobs.jobs.get(match[1]);
      if (!job || req.headers['x-job-token'] !== job.token) return json(res,404,{error:'Job not found.'});
      if (req.method === 'DELETE') jobs.cancel(job.id);
      else if (req.method !== 'GET') return json(res,405,{error:'Method not allowed.'});
      return json(res,200,{id:job.id,status:job.status,result:job.result,error:job.error});
    }
    if (pathname.startsWith('/api/')) return json(res,404,{error:'Unknown API route.'});
    const output = /^\/output\/([\w-]+)\/((?:output|pose-reference|costume-reference)\.(?:png|jpg|webp))$/.exec(pathname);
    if (output && req.method === 'GET') { await serve(res,path.join(appRoot,'output'),`${output[1]}/${output[2]}`); return; }
    const extraction = /^\/results\/([\w-]+)\/output.png$/.exec(pathname);
    if (extraction && req.method === 'GET') { await serve(res,path.join(appRoot,'runtime/extractions'),`${extraction[1]}/output.png`); return; }
    if (req.method !== 'GET' && req.method !== 'HEAD') return json(res,405,{error:'Method not allowed.'});
    for (const [prefix, base] of [['/references/',upstream],['/characters/',path.join(root,'characters')],['/custom/',path.join(upstream,'public/custom')],['/brand/',path.join(upstream,'public/brand')],['/images/',path.join(upstream,'public/images')],['/guide/',path.join(upstream,'public/guide')]]) {
      if (pathname.startsWith(prefix)) { await serve(res,base,pathname.slice(prefix.length)); return; }
    }
    if (vite) return vite.middlewares(req,res,() => json(res,404,{error:'Not found.'}));
    const relative = pathname === '/' ? 'index.html' : pathname.replace(/^\//,'');
    await serve(res,path.join(appRoot,'dist'),relative);
  } catch (error) {
    if (!res.headersSent) json(res,error.status || (error.code === 'ENOENT' ? 404 : 400),{error:error.message});
    else res.end();
  }
});
server.on('error', error => { console.error(error.message); process.exitCode = 1; void vite?.close(); });
server.listen(port,'127.0.0.1',() => console.log(`Silicon Wars · Pose & Costume\n  Local: ${origin}\n  Codex: ${codexBinary}`));
const close = () => { jobs.close(); server.close(); void vite?.close(); };
process.on('SIGINT',close); process.on('SIGTERM',close);
