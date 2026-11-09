"""Download real NASA archive images; preserve original metadata and attribution."""
import requests,json,concurrent.futures,pathlib,io
from PIL import Image,ImageDraw
ROOT=pathlib.Path(__file__).resolve().parents[1]
IDS={'sun':'GSFC_20171208_Archive_e002035','mercury':'PIA15162','earth':'PIA00122','mars':'PIA00407','jupiter':'PIA22946','saturn':'PIA11141','neptune':'PIA01492','pluto':'PIA19952','moon':'PIA00405','comet':'PIA18899','stars':'PIA09262','milkyway':'iss073e0982261','andromeda':'PIA04921'}
def one(pair):
 key,nasa=pair
 j=requests.get('https://images-api.nasa.gov/search',params={'nasa_id':nasa,'media_type':'image'},timeout=60).json();items=j['collection']['items']
 if not items:raise ValueError(key+' not found '+nasa)
 item=items[0];data=item['data'][0]
 assets=requests.get(item['href'],timeout=60).json();hrefs=assets if isinstance(assets,list) else [a['href'] for a in assets['collection']['items']]
 candidates=[u for u in hrefs if '~medium.jpg' in u]or[u for u in hrefs if '~orig.jpg' in u]or[u for u in hrefs if u.lower().endswith('.jpg')]
 url=candidates[0];raw=requests.get(url,timeout=90);raw.raise_for_status();im=Image.open(io.BytesIO(raw.content)).convert('RGB');size=im.size;im.thumbnail((1400,1400),Image.Resampling.LANCZOS);im.save(ROOT/f'public/photos/{key}.webp',quality=88)
 print(key,nasa,data['title'],size,flush=True)
 return key,{'nasaId':nasa,'source':f'https://images.nasa.gov/details/{nasa}','download':url,'title':data['title'],'description':data.get('description',''),'creator':data.get('secondary_creator',data.get('center','NASA')),'originalSize':size}
out={}
for k,v in concurrent.futures.ThreadPoolExecutor(5).map(one,IDS.items()):out[k]=v
(ROOT/'art-source/photo-metadata.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
# Contact sheet for factual identity/quality review.
sheet=Image.new('RGB',(1000,4*190),'#0b1428');draw=ImageDraw.Draw(sheet)
for i,key in enumerate(IDS):
 im=Image.open(ROOT/f'public/photos/{key}.webp');im.thumbnail((180,155));x=(i%5)*200+(200-im.width)//2;y=(i//5)*190;sheet.paste(im,(x,y));draw.text(((i%5)*200+10,y+160),key,fill='white')
sheet.save(ROOT/'art-source/photo-contact.jpg')

# Always apply the reviewed single-planet and actual-photo replacements.
import subprocess,sys
subprocess.run([sys.executable,str(ROOT/'scripts/curate-photos.py')],check=True)
