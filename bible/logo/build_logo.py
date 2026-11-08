import sys
from shapely.geometry import LineString, MultiPolygon, box
from shapely.ops import unary_union
from shapely import affinity
from shapely.affinity import affine_transform

T=36        # stroke weight
H=100       # cap height (centerline)
SHEAR=0.26
GAP=10
C=18        # chamfer

def chamfer(pts,c=C):
    out=[pts[0]]
    for i in range(1,len(pts)-1):
        p0,p1,p2=pts[i-1],pts[i],pts[i+1]
        def toward(a,b):
            dx,dy=b[0]-a[0],b[1]-a[1]; L=(dx*dx+dy*dy)**.5
            k=min(c,L/2.5)/L; return (a[0]+dx*k,a[1]+dy*k)
        out+= [toward(p1,p0),toward(p1,p2)]
    out.append(pts[-1]); return out

def glyph(ch,w,h):
    if ch=='I': ls=[[(0,0),(0,h)]]
    elif ch=='L': ls=[[(0,0),(0,h),(w,h)]]
    elif ch=='S': ls=[chamfer([(w,0),(0,0),(0,h/2),(w,h/2),(w,h),(0,h)])]
    elif ch=='C': ls=[chamfer([(w,0),(0,0),(0,h),(w,h)])]
    elif ch=='O': ls=[chamfer([(0,0),(w,0),(w,h),(0,h),(0,0)])]
    elif ch=='N': ls=[[(0,h),(0,0),(w,h),(w,0)]]
    elif ch=='W': ls=[[(0,0),(.26*w,h),(.5*w,.3*h),(.74*w,h),(w,0)]]
    elif ch=='A': ls=[[(0,h),(.5*w,0),(w,h)],[(.2*w,.76*h),(.8*w,.76*h)]]
    elif ch=='R': ls=[chamfer([(0,h),(0,0),(w,0),(w,h/2),(0,h/2)]),[(.42*w,h/2),(w,h)]]
    g=unary_union([LineString(p).buffer(T/2,cap_style=2,join_style=2,mitre_limit=2.6) for p in ls])
    if ch in 'NAR': g=g.intersection(box(-T,0,w+T,h))
    if ch=='W': g=g.intersection(box(-T,0,w+T,h+T*0.9))
    return g

def line(text,widths,h):
    gs=[];x=0
    for ch,w in zip(text,widths):
        g=glyph(ch,w,h)
        g=affine_transform(g,[1,-SHEAR,0,1,SHEAR*h,0])
        minx=g.bounds[0]; g=affinity.translate(g,x-minx,0)
        gs.append(g); x=g.bounds[2]+GAP
    return gs

def group_bounds(gs):
    return unary_union(gs).bounds

def d_of(geom):
    ds=[]
    for p in (geom.geoms if isinstance(geom,MultiPolygon) else [geom]):
        for r in [p.exterior]+list(p.interiors):
            c=list(r.coords)[:-1]; ds.append('M'+' L'.join(f'{x:.1f},{y:.1f}' for x,y in c)+' Z')
    return ' '.join(ds)

H2=128
l1=line('SILICON',[80,0,64,0,70,76,74],H)
b1=group_bounds(l1); w1=b1[2]-b1[0]
def make_l2(ww):
    k=ww/100.0
    return line('WARS',[130*k,100*k,84*k,96*k],H2)
lo,hi=30,300
for _ in range(40):
    mid=(lo+hi)/2; g=make_l2(mid); bb=group_bounds(g)
    if bb[2]-bb[0]<w1: lo=mid
    else: hi=mid
l2=make_l2((lo+hi)/2); b2=group_bounds(l2)
l2=[affinity.translate(g,b1[0]-b2[0],(b1[3]-b2[1])+26) for g in l2]
allg=unary_union(l1+l2); mnx,mny,mxx,mxy=allg.bounds
pad=40
vb=(mnx-pad,mny-pad,mxx-mnx+2*pad,mxy-mny+2*pad)
outer=''.join(f'    <path d="{d_of(g)}"/>\n' for g in l1+l2)
inner=''.join(f'    <path d="{d_of(g.buffer(-7,join_style=2,mitre_limit=2))}"/>\n' for g in l1+l2 if not g.buffer(-7).is_empty)
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]:.0f} {vb[1]:.0f} {vb[2]:.0f} {vb[3]:.0f}" width="{vb[2]:.0f}" height="{vb[3]:.0f}">
  <title>Silicon Wars</title>
  <rect x="{vb[0]:.0f}" y="{vb[1]:.0f}" width="{vb[2]:.0f}" height="{vb[3]:.0f}" fill="#fff"/>
  <g fill="none" stroke="#000" stroke-linejoin="miter" fill-rule="evenodd">
    <g stroke-width="4">
{outer}    </g>
    <g stroke-width="1.6">
{inner}    </g>
  </g>
</svg>
'''
open(sys.argv[1],'w').write(svg)
print(vb)
