import { readFile, access } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

export const root = fileURLToPath(new URL('../../', import.meta.url));
export const upstream = path.join(root, 'external/open-pose-costume');
const exists = async (file) => { try { await access(file); return true; } catch { return false; } };
const localized = (text) => ({ en: text, zh: text });

export async function loadCatalog(origin) {
  const catalog = JSON.parse(await readFile(path.join(upstream, 'public/data/catalog.json'), 'utf8'));
  const roster = JSON.parse(await readFile(path.join(root, 'characters/roster.json'), 'utf8'));
  const resolveAsset = async (value, kind, thumbnail = false) => {
    if (!value.startsWith('http')) return new URL(`/${value}`, origin).href;
    const filename = path.basename(new URL(value).pathname);
    const relative = `${kind}/${thumbnail ? 'covers' : 'originals'}/${filename}`;
    if (await exists(path.join(upstream, relative))) return new URL(`/references/${relative}`, origin).href;
    if (!thumbnail && await exists(path.join(upstream, `${kind}/covers/${filename}`))) return new URL(`/references/${kind}/covers/${filename}`, origin).href;
    // Not every gallery original is vendored. Retain the upstream URL in that case.
    return value;
  };
  const items = await Promise.all(catalog.items.filter(item => item.kind !== 'character').map(async item => ({
    ...item,
    variants: await Promise.all(item.variants.map(async variant => {
      const resolved = { ...variant };
      for (const key of ['thumbnail', 'image', 'original']) resolved[key] = await resolveAsset(variant[key], item.kind, key === 'thumbnail');
      if (variant.depth) {
        resolved.depth = { ...variant.depth };
        for (const key of ['thumbnail', 'image', 'original']) resolved.depth[key] = await resolveAsset(variant.depth[key], item.kind, key === 'thumbnail');
      } else if (item.kind === 'pose' && variant.original.startsWith('https://ai-pose-gallery.pages.dev/')) {
        resolved.depth = Object.fromEntries(['thumbnail', 'image', 'original'].map(key => [key, variant[key].replace('ai-pose-gallery.', 'ai-pose-depth-gallery.')]));
      }
      return resolved;
    })),
  })));
  for (const character of roster) {
    const folder = path.join(root, 'characters', character.slug);
    const art = await exists(path.join(folder, 'character_sheet.png')) ? 'character_sheet.png' : 'reference_card.jpg';
    if (!await exists(path.join(folder, art))) throw Error(`Missing character art: ${character.slug}`);
    const url = new URL(`/characters/${character.slug}/${art}`, origin).href;
    items.push({ id: `sw-${character.slug}`, kind: 'character', code: character.name,
      title: localized(character.name), category: {id: 'silicon-wars', ...localized('Silicon Wars')},
      series: localized(character.title), extended: false, source: `/characters/${character.slug}/README.md`,
      keywords: localized(`${character.title} ${character.faction} ${character.hair} ${character.appearance} ${character.age}`),
      tags: [{id: 'female', ...localized('Female')}, {id: 'anime', ...localized('Anime')}],
      variants: [{id: `sw-${character.slug}-identity`, angle: 'front', label: localized('Canonical model sheet'), thumbnail: url, image: url, original: url}],
    });
  }
  const stats = {poseGroups: items.filter(i => i.kind === 'pose').length,
    poseImages: items.filter(i => i.kind === 'pose').reduce((n, i) => n+i.variants.length, 0),
    costumes: items.filter(i => i.kind === 'costume').length, characters: roster.length,
    references: items.length, images: items.reduce((n, i) => n+i.variants.length, 0)};
  return {items, stats};
}

export function referenceIndex(catalog) {
  const index = new Map();
  for (const item of catalog.items) for (const variant of item.variants) {
    index.set(`${item.kind}:${variant.id}:${variant.original}`, {kind: item.kind, itemId: item.id, variantId: variant.id, url: variant.original});
    if (variant.depth) index.set(`${item.kind}:${variant.id}:${variant.depth.original}`, {kind: item.kind, itemId: item.id, variantId: variant.id, url: variant.depth.original, depth: true});
  }
  return index;
}

export function localFile(url, origin) {
  const parsed = new URL(url, origin);
  if (parsed.origin !== origin || parsed.search || parsed.hash) return null;
  const mappings = [['/characters/', path.join(root, 'characters')], ['/references/', upstream], ['/custom/', path.join(upstream, 'public/custom')]];
  for (const [prefix, base] of mappings) {
    if (!parsed.pathname.startsWith(prefix)) continue;
    const resolved = path.resolve(base, decodeURIComponent(parsed.pathname.slice(prefix.length)));
    if (!resolved.startsWith(`${path.resolve(base)}${path.sep}`)) return null;
    return resolved;
  }
  return null;
}
