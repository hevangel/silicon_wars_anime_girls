from PIL import Image, ImageDraw
import os
os.makedirs('scratchpad', exist_ok=True)
specs = {
 'intel':  ('characters/intel/character_sheet.png',  (292, 16, 492, 388)),
 'amd':    ('characters/amd/character_sheet.png',    (362, 16, 548, 502)),
 'nvidia': ('characters/nvidia/character_sheet.png', (362, 6, 534, 452)),
}
for name,(path,box) in specs.items():
    im = Image.open(path).convert('RGB')
    print(name, im.size, box)
    im.crop(box).resize(((box[2]-box[0])*2, (box[3]-box[1])*2), Image.LANCZOS).save(f'scratchpad/_body_{name}.jpg', quality=95)
