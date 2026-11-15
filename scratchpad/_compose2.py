from PIL import Image, ImageDraw
import os
bodies = {
 'intel':  ('characters/intel/character_sheet.png',  (640, 20, 1005, 780)),
 'amd':    ('characters/amd/character_sheet.png',    (775, 20, 1072, 660)),
 'nvidia': ('characters/nvidia/character_sheet.png', (770, 10, 1082, 642)),
}
grids = {
 'intel':  ('characters/intel/expressions.png',  591, 1909),
 'amd':    ('characters/amd/expressions.png',    620, 1911),
 'nvidia': ('characters/nvidia/expressions.png', 659, 1911),
}
picks = {
 'intel':  [(1,2),(2,1),(1,0)],
 'amd':    [(1,0),(2,0),(3,1)],
 'nvidia': [(2,0),(3,1),(2,2)],
}
COL=440; BODY_H=800; HEAD_H=120
sheet = Image.new('RGB', (COL*3+40, BODY_H+HEAD_H+60), 'white')
for i,name in enumerate(['intel','amd','nvidia']):
    x = 10 + i*(COL+10)
    path,box = bodies[name]
    b = Image.open(path).convert('RGB').crop(box)
    b.thumbnail((COL, BODY_H), Image.LANCZOS)
    sheet.paste(b, (x + (COL-b.width)//2, 10 + (BODY_H-b.height)//2))
    path2,x0,x1 = grids[name]
    im = Image.open(path2).convert('RGB')
    w=(x1-x0)/3.0; h=(1270-17)/4.0
    for j,(r,c) in enumerate(picks[name]):
        hb=(int(x0+c*w+14), int(17+r*h+54), int(x0+(c+1)*w-22), int(17+(r+1)*h-14))
        hd=im.crop(hb)
        hd.thumbnail((COL//3-6, HEAD_H), Image.LANCZOS)
        sheet.paste(hd, (x + j*(COL//3) + (COL//3-hd.width)//2, 10+BODY_H+30))
    ImageDraw.Draw(sheet).line((x-5,10,x-5,BODY_H+HEAD_H+40), fill=(228,228,228), width=2)
os.makedirs('chapters/pilot-005/pages/page-001/refs', exist_ok=True)
sheet.save('chapters/pilot-005/pages/page-001/refs/cast-reference.jpg', quality=94)
print(sheet.size)
