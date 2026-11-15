from PIL import Image
boxes = {
 'intel':  ('characters/intel/character_sheet.png',  (640, 20, 1005, 805)),
 'amd':    ('characters/amd/character_sheet.png',    (775, 20, 1072, 1030)),
 'nvidia': ('characters/nvidia/character_sheet.png', (770, 10, 1082, 928)),
}
crops=[]
for name,(path,b) in boxes.items():
    im = Image.open(path).convert('RGB').crop(b)
    im.thumbnail((300,860), Image.LANCZOS)
    crops.append(im)
W=sum(c.width for c in crops)+40; H=max(c.height for c in crops)+20
sheet=Image.new('RGB',(W,H),'white'); x=10
for c in crops:
    sheet.paste(c,(x,10)); x+=c.width+10
sheet.save('scratchpad/_bodies_preview.jpg', quality=94)
print(sheet.size, [c.size for c in crops])
