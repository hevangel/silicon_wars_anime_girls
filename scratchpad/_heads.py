from PIL import Image
grids = {
 'intel':  ('characters/intel/expressions.png',  591, 1909),
 'amd':    ('characters/amd/expressions.png',    620, 1911),
 'nvidia': ('characters/nvidia/expressions.png', 659, 1911),
}
picks = {
 'intel':  [(1,2),(2,1),(1,0)],   # surprised, flustered, angry
 'amd':    [(1,0),(2,0),(3,1)],   # angry, smug, excited
 'nvidia': [(2,0),(3,1),(2,2)],   # smug, excited, serious
}
top, bottom = 17, 1270
saved={}
for name,(path,x0,x1) in grids.items():
    im = Image.open(path).convert('RGB')
    w = (x1-x0)/3.0
    h = (bottom-top)/4.0
    heads=[]
    for (r,c) in picks[name]:
        box = (int(x0+c*w+6), int(top+r*h+46), int(x0+(c+1)*w-6), int(top+(r+1)*h-8))
        crop = im.crop(box)
        heads.append(crop)
        print(name,(r,c),crop.size)
    saved[name]=heads

# preview strip
W=3*300+40; H=3*240+40
prev=Image.new('RGB',(W,H),'white')
for i,name in enumerate(['intel','amd','nvidia']):
    for j,hd in enumerate(saved[name]):
        t=hd.copy(); t.thumbnail((280,220), Image.LANCZOS)
        prev.paste(t,(10+j*300, 10+i*240))
prev.save('scratchpad/_heads_preview.jpg', quality=94)
print(prev.size)
