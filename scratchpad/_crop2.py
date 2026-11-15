from PIL import Image
boxes = {
 'intel':  ('characters/intel/character_sheet.png',  (600, 20, 1010, 820)),
 'amd':    ('characters/amd/character_sheet.png',    (760, 20, 1140, 1060)),
 'nvidia': ('characters/nvidia/character_sheet.png', (760, 10, 1110, 950)),
}
for name,(path,b) in boxes.items():
    im = Image.open(path).convert('RGB').crop(b)
    im.thumbnail((420,900), Image.LANCZOS)
    im.save(f'scratchpad/_body_{name}.jpg', quality=94)
    print(name, im.size)
