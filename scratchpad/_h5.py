import hashlib, pathlib, yaml
root=pathlib.Path('.')
def h(p): return hashlib.sha256((root/p).read_bytes()).hexdigest()
brief=yaml.safe_load(open('chapters/pilot-005/pages/page-001/panels/panel-01.yaml',encoding='utf-8'))
print('prompt', hashlib.sha256(brief['direction'].encode()).hexdigest())
for p in ['chapters/pilot-005/pages/page-001/refs/cast-reference.jpg',
          'chapters/pilot-005/pages/page-001/art/panel-01.png',
          'chapters/pilot-005/pages/page-001/final/page-001.png']:
    print(h(p), p, (root/p).stat().st_size)
for c in ['intel','amd','nvidia']:
    print(h(f'characters/{c}/character_sheet.png'), f'characters/{c}/character_sheet.png')
for c in ['intel','amd','nvidia']:
    print(h(f'characters/{c}/expressions.png'), f'characters/{c}/expressions.png')
import PIL; print('pillow', PIL.__version__)
