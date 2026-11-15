import { ImageGenerationError, type ImageConfig, type ImageReference } from './generation';

export async function localGenerate(config: ImageConfig, references: ImageReference[], prompt: string, signal: AbortSignal, fetcher: typeof fetch): Promise<string> {
  const form = new FormData();
  form.set('prompt', prompt);
  form.set('size', config.size);
  form.set('quality', config.quality);
  if (references.length === 1 && references[0].kind === 'costume' && 'file' in references[0]) form.set('mode', 'extract-costume');
  form.set('references', JSON.stringify(references.map((ref, index) => {
    if ('file' in ref) { form.set(`upload-${index}`, ref.file); return { kind: ref.kind, upload: `upload-${index}` }; }
    return { kind: ref.kind, id: ref.variant.id, url: ref.variant.original };
  })));
  const response = await fetcher('/api/jobs', {method: 'POST', body: form, signal});
  const submitted = await response.json();
  if (!response.ok) throw new ImageGenerationError('providerFailed', submitted.error);
  const endpoint = `/api/jobs/${submitted.id}`;
  const cancel = () => { void fetcher(endpoint, {method: 'DELETE', headers: {'X-Job-Token': submitted.token}, keepalive: true}).catch(() => undefined); };
  signal.addEventListener('abort', cancel, {once: true});
  try {
    if (signal.aborted) { cancel(); signal.throwIfAborted(); }
    while (true) {
      const statusResponse = await fetcher(endpoint, {signal, headers: {'X-Job-Token': submitted.token}});
      const job = await statusResponse.json();
      if (!statusResponse.ok || job.status === 'failed') throw new ImageGenerationError('providerFailed', job.error || 'Local generation failed');
      if (job.status === 'cancelled') throw new ImageGenerationError('cancelled');
      if (job.status === 'succeeded') return job.result;
      await new Promise<void>((resolve, reject) => {
        const abort = () => { clearTimeout(timer); reject(signal.reason); };
        const timer = setTimeout(() => { signal.removeEventListener('abort', abort); resolve(); }, 1000);
        signal.addEventListener('abort', abort, {once: true});
      });
    }
  } finally { signal.removeEventListener('abort', cancel); }
}
