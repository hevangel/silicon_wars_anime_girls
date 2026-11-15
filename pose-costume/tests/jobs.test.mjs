import test from 'node:test';
import assert from 'node:assert/strict';
import { EventEmitter } from 'node:events';
import { PassThrough } from 'node:stream';
import { mkdtemp, readFile, writeFile, rm } from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { loadCatalog, localFile, referenceIndex } from '../server/catalog.mjs';
import { JobManager, codexArguments } from '../server/jobs.mjs';

const origin = 'http://127.0.0.1:5200';
const catalog = await loadCatalog(origin);
const png = Buffer.from('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Y9Z4ZIAAAAASUVORK5CYII=', 'base64');
const refs = ['pose','costume','character'].map(kind => {
  const item = catalog.items.find(i => i.kind === kind && i.variants[0].original.startsWith(origin));
  return {kind, id:item.variants[0].id, url:item.variants[0].original};
});
const input = {prompt:'Test the selected pose, outfit and canonical identity.', size:'1024x1536',quality:'auto',references:refs};

test('catalog retains upstream pose and costume IDs while replacing all characters', () => {
  assert.equal(catalog.stats.characters,32);
  assert.equal(catalog.stats.poseGroups,343);
  assert.equal(catalog.stats.costumes,2801);
  assert.equal(catalog.items.filter(i => i.kind === 'character').every(i => i.id.startsWith('sw-')),true);
  assert.equal(new Set(catalog.items.map(i => i.id)).size,catalog.items.length);
  assert.ok(referenceIndex(catalog).size > catalog.items.length);
});

test('rejects arbitrary URLs, uploaded identities and incomplete selections', () => {
  const manager = new JobManager(catalog,origin);
  assert.throws(() => manager.validate({...input,references:refs.slice(0,2)}), /one pose/);
  assert.throws(() => manager.validate({...input,references:refs.map(r => r.kind === 'character' ? {...r,url:'http://169.254.169.254/'} : r)}),/catalog/);
  assert.throws(() => manager.validate({...input,references:refs.map(r => r.kind === 'character' ? {kind:'character',upload:'file'} : r)}),/catalog/);
  assert.throws(() => manager.validate({...input,size:'shell-command'}),/Invalid/);
  assert.equal(localFile(`${origin}/references/%2e%2e%2f.git/config`,origin),null);
});

test('Codex job attaches references, saves provenance and requires an actual PNG', async t => {
  const outputRoot = await mkdtemp(path.join(os.tmpdir(),'swpc-'));
  t.after(() => rm(outputRoot,{recursive:true,force:true}));
  let invocation;
  const launch = (binary,args,options) => {
    invocation = {binary,args,options};
    const child = new EventEmitter(); child.stdout = new PassThrough(); child.stderr = new PassThrough(); child.stdin = new PassThrough(); child.stdin.resume();
    child.stdin.on('finish', () => { void writeFile(path.join(options.cwd,'output.png'),png).then(() => child.emit('close',0)); });
    return child;
  };
  const manager = new JobManager(catalog,origin,{launch,binary:'test-codex',outputRoot});
  const submitted = await manager.submit(input);
  await assert.rejects(manager.submit(input), /already running/);
  const job = manager.jobs.get(submitted.id); await job.done;
  assert.equal(job.status,'succeeded');
  assert.equal(job.directory,path.join(outputRoot,submitted.id));
  assert.equal(job.result,`/output/${submitted.id}/output.png`);
  assert.equal(invocation.options.shell,false);
  assert.equal(invocation.args.filter(a => a === '--image').length,3);
  assert.ok(invocation.args.includes('workspace-write'));
  assert.ok(!invocation.args.includes('--dangerously-bypass-approvals-and-sandbox'));
  const manifest = JSON.parse(await readFile(path.join(job.directory,'generation.json'),'utf8'));
  assert.equal(manifest.identity.slug,'intel');
  assert.equal(manifest.references.length,3);
  assert.ok(manifest.references.every(r => /^[a-f0-9]{64}$/.test(r.sha256)));
  assert.equal(manifest.lettering.mode,'none');
  assert.ok(manifest.output.sha256);
  assert.match(await readFile(path.join(job.directory,'generation.prompt.md'),'utf8'),/SERIES CONTINUITY/);
});

test('a successful CLI exit without generated art is a failed job', async t => {
  const outputRoot = await mkdtemp(path.join(os.tmpdir(),'swpc-'));
  t.after(() => rm(outputRoot,{recursive:true,force:true}));
  const launch = () => {
    const child = new EventEmitter(); child.stdout = new PassThrough(); child.stderr = new PassThrough(); child.stdin = new PassThrough(); child.stdin.resume();
    child.stdin.on('finish',() => child.emit('close',0)); return child;
  };
  const manager = new JobManager(catalog,origin,{launch,outputRoot});
  const {id} = await manager.submit(input); const job = manager.jobs.get(id); await job.done;
  assert.equal(job.status,'failed'); assert.match(job.error,/did not save/);
});

test('cancelling preparation prevents spawning Codex', async t => {
  const outputRoot = await mkdtemp(path.join(os.tmpdir(),'swpc-'));
  t.after(() => rm(outputRoot,{recursive:true,force:true}));
  const manager = new JobManager(catalog,origin,{outputRoot,launch:() => {throw Error('must not launch');}});
  const {id} = await manager.submit(input); manager.cancel(id); const job = manager.jobs.get(id); await job.done;
  assert.equal(job.status,'cancelled'); assert.equal(manager.busy,false);
});

test('file paths are separate CLI arguments', () => {
  const args = codexArguments('C:/My Art/job',['C:/My Art/pose.png','C:/My Art/identity.png']);
  assert.equal(args.at(-1),'-'); assert.ok(args.includes('C:/My Art/identity.png'));
});

test('uploaded costumes and costume-only extraction use local Codex jobs', async t => {
  const outputRoot = await mkdtemp(path.join(os.tmpdir(),'swpc-'));
  t.after(() => rm(outputRoot,{recursive:true,force:true}));
  const launch = (_binary,_args,options) => {
    const child = new EventEmitter(); child.stdout = new PassThrough(); child.stderr = new PassThrough(); child.stdin = new PassThrough(); child.stdin.resume();
    child.stdin.on('finish',() => { void writeFile(path.join(options.cwd,'output.png'),png).then(() => child.emit('close',0)); });
    return child;
  };
  const manager = new JobManager(catalog,origin,{launch,outputRoot});
  const costume = {kind:'costume',uploadData:png,extension:'.png'};
  const normal = await manager.submit({...input,references:refs.map(r => r.kind === 'costume' ? costume : r)});
  const normalJob = manager.jobs.get(normal.id); await normalJob.done;
  assert.equal(normalJob.status,'succeeded');
  assert.deepEqual(await readFile(path.join(normalJob.directory,'costume-reference.png')),png);
  const extraction = await manager.submit({...input,mode:'extract-costume',references:[costume]});
  const extractionJob = manager.jobs.get(extraction.id); await extractionJob.done;
  assert.equal(extractionJob.status,'succeeded');
  assert.equal(extractionJob.directory,path.join(outputRoot,extraction.id));
  assert.equal(extractionJob.result,`/output/${extraction.id}/output.png`);
  assert.match(await readFile(path.join(extractionJob.directory,'generation.prompt.md'),'utf8'),/No person, face, skin or mannequin/);
});
