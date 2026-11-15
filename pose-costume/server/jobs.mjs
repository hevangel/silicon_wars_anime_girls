import { spawn, execFile } from 'node:child_process';
import { randomUUID, createHash } from 'node:crypto';
import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { root, localFile, referenceIndex } from './catalog.mjs';

const PNG = Buffer.from([137,80,78,71,13,10,26,10]);
const hash = bytes => createHash('sha256').update(bytes).digest('hex');
const sizes = ['1024x1024', '1024x1536', '1536x1024', '2048x2048', 'auto'];
export const codexBinary = process.env.CODEX_BIN || 'codex';

export function stopProcess(child) {
  if (!child?.pid) return;
  if (process.platform === 'win32') execFile('taskkill', ['/PID', String(child.pid), '/T', '/F'], () => {});
  else { try { process.kill(-child.pid, 'SIGTERM'); } catch { child.kill('SIGTERM'); } }
}

export function codexArguments(directory, images) {
  return ['exec', '--ephemeral', '--sandbox', 'workspace-write', '-C', directory,
    '--color', 'never', ...images.flatMap(file => ['--image', file]), '-'];
}

export class JobManager {
  constructor(catalog, origin, {launch = spawn, binary = codexBinary, outputRoot = path.join(root, 'pose-costume/output'), timeoutMs = 15 * 60_000} = {}) {
    this.index = referenceIndex(catalog); this.origin = origin; this.launch = launch;
    this.binary = binary; this.outputRoot = outputRoot; this.timeoutMs = timeoutMs;
    this.jobs = new Map(); this.busy = false;
  }

  validate(input) {
    if (typeof input.prompt !== 'string' || !input.prompt.trim() || input.prompt.length > 20000) throw Error('A prompt of 1–20,000 characters is required.');
    if (!sizes.includes(input.size) || !['auto','low','medium','high'].includes(input.quality)) throw Error('Invalid size or quality.');
    const extraction = input.mode === 'extract-costume';
    if (!Array.isArray(input.references) || (extraction ? input.references.length !== 1 || input.references[0].kind !== 'costume' : input.references.length !== 3 || new Set(input.references.map(r => r.kind)).size !== 3)) throw Error('Choose one pose, one costume and one Silicon Wars character.');
    return input.references.map(ref => {
      if (ref.kind === 'costume' && Buffer.isBuffer(ref.uploadData) && ['.png','.jpg','.webp'].includes(ref.extension)) return {kind:'costume', uploadData:ref.uploadData, extension:ref.extension};
      const accepted = this.index.get(`${ref.kind}:${ref.id}:${ref.url}`);
      if (!accepted) throw Error('Only catalog references are accepted. Choose a Silicon Wars character.');
      return accepted;
    });
  }

  async submit(input) {
    const references = this.validate(input);
    if (this.busy) throw Object.assign(Error('A local generation is already running. Wait or cancel it first.'), {status: 409});
    this.busy = true;
    const id = randomUUID();
    const slug = references.find(ref => ref.kind === 'character')?.itemId.replace(/^sw-/, '');
    const directory = path.join(this.outputRoot, id);
    const job = {id, token: randomUUID(), status: 'preparing', directory, slug, createdAt: new Date().toISOString()};
    this.jobs.set(id, job);
    // Defer processing so submission can immediately return its cancellable job handle.
    job.done = this.run(job, input, references).finally(() => { this.busy = false; });
    return {id, token: job.token};
  }

  async run(job, input, references) {
    let timer;
    try {
      await mkdir(job.directory, {recursive: true});
      const images = [], provenance = [];
      for (const ref of references) {
        if (job.status === 'cancelled') return;
        let file = ref.url ? localFile(ref.url, this.origin) : null, bytes;
        if (ref.uploadData) { bytes = ref.uploadData; file = path.join(job.directory, `costume-reference${ref.extension}`); await writeFile(file,bytes); }
        else if (file) bytes = await readFile(file);
        else {
          // URLs must match the catalog exactly; redirects may not leave gallery hosts.
          const allowed = new Set(['ai-pose-gallery.pages.dev','ai-pose-depth-gallery.pages.dev','ai-costume-gallery.pages.dev','ai-costume-anime-gallery.pages.dev']);
          if (!allowed.has(new URL(ref.url).hostname)) throw Error('Unsupported reference host.');
          job.fetchController = new AbortController();
          const response = await fetch(ref.url, {redirect: 'error', signal: AbortSignal.any([job.fetchController.signal, AbortSignal.timeout(60000)])});
          if (!response.ok) throw Error(`Reference unavailable (${response.status}): ${ref.variantId}`);
          const chunks = []; let length = 0;
          for await (const chunk of response.body) { length += chunk.length; if (length > 20 * 1024 * 1024) { job.fetchController.abort(); throw Error('Reference exceeds 20 MB.'); } chunks.push(chunk); }
          bytes = Buffer.concat(chunks);
          if (!/^image\/(png|jpeg|webp)/.test(response.headers.get('content-type') || '')) throw Error('Reference is not an image.');
          file = path.join(job.directory, `${ref.kind}-reference${path.extname(new URL(ref.url).pathname)}`);
          await writeFile(file, bytes);
        }
        const {uploadData, ...metadata} = ref;
        images.push(file); provenance.push({...metadata, file, sha256: hash(bytes)});
      }
      const character = JSON.parse(await readFile(path.join(root, 'characters/roster.json'), 'utf8')).find(c => c.slug === job.slug);
      const profile = job.slug ? await readFile(path.join(root, 'characters', job.slug, 'README.md'), 'utf8') : '';
      const bible = await readFile(path.join(root, 'bible/story_bible.md'), 'utf8');
      const output = path.join(job.directory, 'output.png');
      const identity = character ? `Identity reference: ${images[references.findIndex(r => r.kind === 'character')]}. Preserve this character's identity, age, facial features, hair, body proportions, signature company mark and canonical height (${character.height_cm} cm). Outfit references may change garments but must keep the character recognizable.\nPose, costume and identity are separate reference roles. One continuous image with one character, no lettering, watermarks or extra panels. Keep the complete outfit, shoes and accessories inside the frame with margin. For child and middle-school characters, use only wholesome, age-appropriate poses and fully covering clothing; adapt unsuitable reference details accordingly.\n\nCHARACTER IDENTITY\n${JSON.stringify(character)}\n${profile}\n\nSERIES CONTINUITY\n${bible}` : 'Extract costume garments only. No person, face, skin or mannequin. Preserve the outfit as a complete clothing reference.';
      const prompt = `Generate an image with the available built-in image generation tool. This is an image creation task, not a request to write code. If no image generation tool is available, stop and explain that limitation; do not draw a substitute in code.\nSave the actual generated PNG to ${output}. If the tool saves elsewhere, copy it here. Do not modify any other project files. Do not change dependencies, use API keys, or call external image provider APIs.\nRequested size: ${input.size}; quality: ${input.quality}. Treat these as image instructions if the tool has no size controls.\n${identity}\n\nUSER IMAGE BRIEF\n${input.prompt}\n\nREFERENCE ORDER\n${references.map((r,i) => `${i+1}. ${r.kind}: ${images[i]}`).join('\n')}\n\nWhen finished, confirm the saved image path. Do not claim success without a real generated image file.`;
      await writeFile(path.join(job.directory, 'generation.prompt.md'), prompt);
      const manifest = {id: job.id, createdAt: job.createdAt, engine: 'codex exec', character: job.slug,
        size: input.size, quality: input.quality, scene: {prompt: input.prompt}, identity: character,
        lettering: {mode: 'none'}, references: provenance, command: [this.binary, ...codexArguments(job.directory, images)], promptSha256: hash(Buffer.from(prompt))};
      await writeFile(path.join(job.directory, 'generation.json'), JSON.stringify(manifest, null, 2));
      if (job.status === 'cancelled') return;
      job.status = 'generating';
      let log = '';
      const child = this.launch(this.binary, codexArguments(job.directory, images), {cwd: job.directory, shell: false, detached: process.platform !== 'win32', windowsHide: true, stdio: ['pipe','pipe','pipe']});
      job.child = child;
      const append = data => { log = (log + data.toString()).slice(-100000); };
      child.stdout.on('data', append); child.stderr.on('data', append);
      const result = new Promise((resolve, reject) => { child.once('error', reject); child.once('close', code => resolve(code)); });
      child.stdin.on('error', () => {});
      child.stdin.end(prompt);
      timer = setTimeout(() => { job.timedOut = true; stopProcess(child); }, this.timeoutMs);
      const code = await result;
      await writeFile(path.join(job.directory, 'codex.log'), log);
      if (job.status === 'cancelled') return;
      if (job.timedOut) throw Error('Codex generation timed out after 15 minutes. See codex.log beside the generation inputs.');
      if (code !== 0) throw Error(`Codex exited with code ${code}. Check Codex sign-in and image tool availability. See codex.log beside the generation inputs.`);
      let bytes;
      try { bytes = await readFile(output); } catch { throw Error('Codex did not save output.png. Your local Codex CLI session must have an image generation tool. See codex.log for details.'); }
      if (!bytes.subarray(0, 8).equals(PNG) || bytes.length < 32) throw Error('Codex output is not a valid PNG image.');
      job.result = `/output/${job.id}/output.png`;
      job.status = 'succeeded';
      manifest.output = {file: 'output.png', sha256: hash(bytes)};
      await writeFile(path.join(job.directory, 'generation.json'), JSON.stringify(manifest, null, 2));
    } catch (error) {
      if (job.status !== 'cancelled') { job.status = 'failed'; job.error = error.code === 'ENOENT' ? 'Codex CLI or a required reference file was not found. Install Codex, sign in, and check CODEX_BIN.' : error.message; }
    } finally {
      clearTimeout(timer);
      try { await writeFile(path.join(job.directory, 'status.json'), JSON.stringify({status: job.status, error: job.error, result: job.result}, null, 2)); } catch {}
      delete job.child; delete job.fetchController;
    }
  }

  cancel(id) {
    const job = this.jobs.get(id);
    if (!job || !['preparing','generating'].includes(job.status)) return;
    job.status = 'cancelled'; job.fetchController?.abort(); stopProcess(job.child);
  }
  close() { for (const id of this.jobs.keys()) this.cancel(id); }
}
