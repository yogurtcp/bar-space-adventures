"""Extract generated atlas sprites, retain transparency, and prepare install icons. Pillow required."""
from pathlib import Path
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parents[1]
keys=['sun','mercury','venus','earth','mars','jupiter','saturn','uranus','neptune','pluto','moon','asteroid','comet','stars','nebula','milkyway','andromeda','rocket','bar','telescope']
im=Image.open(ROOT/'art-source/space-atlas.png').convert('RGBA');w,h=im.size
for i,key in enumerate(keys):
 x=i%5;y=i//5
 cell=im.crop((round(x*w/5),round(y*h/4),round((x+1)*w/5),round((y+1)*h/4)))
 cell.resize((256,256),Image.Resampling.NEAREST).save(ROOT/f'public/art/{key}.webp',lossless=True)
# A comfortably padded icon with a pixel rocket, isolated from other Bar apps.
rocket=Image.open(ROOT/'public/art/rocket.webp');rocket.thumbnail((320,320),Image.Resampling.NEAREST)
icon=Image.new('RGBA',(512,512),'#0c142b');icon.alpha_composite(rocket,((512-rocket.width)//2,(512-rocket.height)//2))
d=ImageDraw.Draw(icon)
for x,y in [(88,120),(406,88),(92,357),(409,376)]:d.rectangle((x,y,x+7,y+7),fill='#ffce78')
for n in [180,192,512]:icon.resize((n,n),Image.Resampling.NEAREST).convert('RGB').save(ROOT/f'public/icons/{n}.png')
icon.convert('RGB').save(ROOT/'public/icons/maskable.png')
# Reviewed replacements keep Saturn's rings inside the sprite and remove atlas overlap.
rings=Image.open(ROOT/'art-source/ring-atlas.png').convert('RGBA');rw,rh=rings.size
for i,key in enumerate(['saturn','uranus']):
 cell=rings.crop((round(i*rw/2),0,round((i+1)*rw/2),rh));cell.resize((256,256),Image.Resampling.NEAREST).save(ROOT/f'public/art/{key}.webp',lossless=True)
