"""Original cue-led tree -> forest -> numerical-average illustrations.
All values are constructed examples. Authoring times are provisional (135 words/min).
Pass --overrides measured_audio.json after Avatar audio exists.
"""
from pathlib import Path
import json,math,subprocess,importlib.util,argparse
from PIL import Image,ImageDraw,ImageFont
BLUE='#0072B2';ORANGE='#D55E00';GRAY='#9AA2AA';GREEN='#009E73'
FONT='/System/Library/Fonts/Supplemental/Arial.ttf';BOLD='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
if not Path(FONT).exists():
 from matplotlib.font_manager import findfont
 FONT=findfont('DejaVu Sans');BOLD=findfont('DejaVu Sans:bold')
def txt(d,x,y,s,size=28,b=False):d.text((x,y),s,font=ImageFont.truetype(BOLD if b else FONT,size),fill='black',anchor='mm')
def line(d,pts,col=BLUE,w=4):d.line(pts,fill=col,width=w)
def dot(d,x,y,r=8,col=ORANGE):d.ellipse((x-r,y-r,x+r,y+r),fill=col)
def tree(d,x,y,w=150,h=125,variant=0,col=BLUE,grow=1):
 # The diagram explicitly depicts decision nodes and paths, not botanical icons.
 r=max(4,min(9,w/16));root=(x,y);l=(x-w/2,y+h*.45);rr=(x+w/2,y+h*.45)
 for end in [l,rr]:line(d,[root,(root[0]+(end[0]-root[0])*grow,root[1]+(end[1]-root[1])*grow)],col,3)
 for i,node in enumerate([l,rr]):
  if (variant+i)%3!=0:
   for sign in [-1,1]:
    end=(node[0]+sign*w*.22*grow,node[1]+h*.45*grow);line(d,[node,end],col,3);d.rectangle((end[0]-r,end[1]-r,end[0]+r,end[1]+r),outline=col,width=2)
   dot(d,*node,r,col)
  else:d.rectangle((node[0]-r,node[1]-r,node[0]+r,node[1]+r),outline=col,width=3)
 dot(d,*root,r,col)
 return root,l,rr

def render(a,t):
 im=Image.new('RGB',(1480,300),'white');d=ImageDraw.Draw(im);times={x['id']:x['at'] for x in a['stages']};on=lambda k:t>=times[k];q=lambda k,s=3:min(1,max(0,(t-times[k])/s));n=a.get('source_topic_slide',a['slide'])
 if n==7:
  u=sum(t>=x['at'] for x in a['stages']);tree(d,740,65,430,165,0,grow=min(1,(t+1)/3));txt(d,740,20,'One fitted decision tree',30,True)
  txt(d,740,100,'Input question',26)
  if u>=2:txt(d,465,160,'Yes',26);txt(d,1000,160,'No',26)
  if u>=3:txt(d,490,265,'Leaf: stored mean',27);txt(d,1050,265,'Leaf: stored mean',27)
  if u>=4:
   p=q(a['stages'][3]['id']);dot(d,740+(525-740)*p,65+(139-65)*p,10)
 elif n==16:
  expand=q('forest',4) if on('forest') else 0
  txt(d,740,19,('One base learner' if on('base') else 'One decision tree') if not on('forest') else 'A forest contains varied fitted trees',30,True)
  if not on('forest'):
   tree(d,740,75,380,145,0);txt(d,740,267,'Each node asks a question; a leaf stores a numerical prediction.',26)
  else:
   for j in range(7):
    xx=740+(140+j*200-740)*expand;ww=380*(1-expand)+90*expand;hh=145*(1-expand)+85*expand
    if j!=3 and expand<j*.035:continue
    tree(d,xx,80,ww,hh,j if on('random') else 0,col=BLUE if j==3 else GRAY)
    if expand>.9:txt(d,xx,183,f'Tree {j+1}',24)
   if on('case'):
    p=q('case',3)
    for j in range(7):
     xx=140+j*200;i=0 if j%2 else 1;node=(xx-45 if i==0 else xx+45,118.25)
     if (j+i)%3==0:
      pos=(xx+(node[0]-xx)*p,80+(node[1]-80)*p)
     elif p<.5:
      pos=(xx+(node[0]-xx)*p*2,80+(node[1]-80)*p*2)
     else:
      end=(node[0]+(19.8 if j%2 else -19.8),156.5);qq=(p-.5)*2;pos=(node[0]+(end[0]-node[0])*qq,node[1]+(end[1]-node[1])*qq)
     dot(d,*pos,7)
    txt(d,740,225,'The same input case follows each fitted rule.',27,True)
   if on('average'):
    d.rectangle((0,205,1480,299),fill='white')
    for j in range(7):line(d,[(140+j*200,201),(740,255)],'#C0C6CC',2)
    d.rounded_rectangle((475,240,1005,292),radius=8,outline=GREEN,width=3);txt(d,740,266,'Average the numerical predictions',27,True)
 elif n==19:
  txt(d,740,20,'Same prediction case; three illustrative fitted trees',30,True)
  u=sum(t>=x['at'] for x in a['stages'])
  for j,x in enumerate([240,740,1240]):
   dot(d,x,65,7,BLUE)
   for side in [-1,1]:
    end=(x+side*70,143);line(d,[(x,65),end],BLUE,3);d.rectangle((end[0]-7,end[1]-7,end[0]+7,end[1]+7),outline=BLUE,width=2)
   txt(d,x,98,'x ≤ 0?',23);txt(d,x,172,f'Tree {j+1}',26)
   if u>=2:txt(d,x,207,str([50,60,70][j]) if u>=6 else 'One tree prediction',28,True)
  if u>=4:
   for x in [240,740,1240]:line(d,[(x,225),(740,252)],GRAY,2)
  if u>=5:txt(d,740,278,'(50 + 60 + 70) / 3 = 60' if u>=6 else 'Sum the tree predictions, then divide by the tree count',28,True)
 return im
