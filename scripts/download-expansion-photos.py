"""Reviewed observational images and actual spacecraft hardware for the expansion."""
import requests,json,concurrent.futures,pathlib,io
from PIL import Image,ImageDraw
ROOT=pathlib.Path(__file__).resolve().parents[1]
S={
'blackhole':dict(source='https://science.nasa.gov/resource/first-image-of-a-black-hole/',url='https://assets.science.nasa.gov/dynamicimage/assets/science/psd/solar/2023/09/b/blackhole_1600.jpg?w=1600&h=932&fit=clip',credit='Event Horizon Telescope Collaboration',he='M87 · שחזור תצפיות בטלסקופי רדיו',en='M87 · reconstructed radio observations'),
'quasar':dict(source='https://science.nasa.gov/missions/hubble/nasas-hubble-gets-the-best-image-of-bright-quasar-3c-273/',url='https://science.nasa.gov/wp-content/uploads/2023/04/potw1346a-jpg.webp?w=1280',credit='ESA/Hubble & NASA',he='הקוואזר 3C 273 · צילום האבל',en='Quasar 3C 273 · Hubble observations'),
'betelgeuse':dict(source='https://www.eso.org/public/images/potw1726a/',url='https://cdn.eso.org/images/thumb700x/potw1726a.jpg',credit='ALMA (ESO/NAOJ/NRAO)/E. O’Gorman/P. Kervella',he='ביטלג׳וז · תצפית ALMA בצבעים מעובדים',en='Betelgeuse · processed-color ALMA image'),
'sirius':dict(source='https://esahubble.org/images/heic0516a/',url='https://cdn.esahubble.org/archives/images/thumb700x/heic0516a.jpg',credit='NASA, ESA, H. Bond (STScI), and M. Barstow (University of Leicester)',he='סיריוס ובן לווייתו · צילום האבל',en='Sirius and its companion · Hubble image'),
'polaris':dict(source='https://science.nasa.gov/asset/hubble/polaris-a-and-polaris-b/',url='https://assets.science.nasa.gov/dynamicimage/assets/science/missions/hubble/releases/2006/01/STScI-01EVT7S8K23VFHYY7QKWCZF1PN.tif?w=1400',credit='NASA, ESA, N. Evans (Harvard-Smithsonian CfA), and H. Bond (STScI)',he='כוכב הצפון ובן לווייתו · צילום האבל',en='Polaris and companion · Hubble image'),
'satellite':dict(nasa='KSC-20210811-PH-RNB01_0028',credit='NASA / Kennedy Space Center',he='לנדסאט 9 · צילום לפני השיגור',en='Landsat 9 · prelaunch hardware photograph'),
'iss':dict(source='https://www.nasa.gov/international-space-station/space-station-facts-and-figures/',url='https://www.nasa.gov/wp-content/uploads/2020/11/iss-7.jpg?w=1400',credit='NASA',he='תחנת החלל הבינלאומית · צילום ממסלול',en='International Space Station · orbital photograph'),
'hubble':dict(source='https://science.nasa.gov/mission/hubble/',url='https://science.nasa.gov/wp-content/uploads/2023/07/hubble-space-telescope-hst-6.jpg?w=1280',credit='NASA',he='טלסקופ החלל האבל · צילום ממסלול',en='Hubble Space Telescope · orbital photograph'),
'webb':dict(source='https://science.nasa.gov/mission/webb/',url='https://science.nasa.gov/wp-content/uploads/2023/06/webb-flickr-47543984121-1f8e7757bc-4k-jpg.webp?w=1400',credit='NASA',he='טלסקופ ווב · צילום לפני השיגור',en='Webb telescope · prelaunch hardware photograph'),
'perseverance':dict(nasa='PIA24542',credit='NASA / JPL-Caltech / MSSS',he='פרסווירנס על מאדים · פסיפס צילומים',en='Perseverance on Mars · selfie mosaic'),
'curiosity':dict(nasa='PIA23240',credit='NASA / JPL-Caltech / MSSS',he='קיוריוסיטי על מאדים · פסיפס צילומים',en='Curiosity on Mars · selfie mosaic'),
'ingenuity':dict(nasa='PIA24581',credit='NASA / JPL-Caltech / ASU',he='אינג׳ניואיטי על מאדים · צילום מהרובוט',en='Ingenuity on Mars · rover photograph'),
'voyager':dict(nasa='PIA21737',credit='NASA / JPL-Caltech',he='גשושית ממשפחת וויאג׳ר · בדיקות ב־1977',en='Voyager-family spacecraft · 1977 ground test')}
def one(pair):
 k,d=pair
 if 'nasa'in d:
  items=requests.get('https://images-api.nasa.gov/search',params={'nasa_id':d['nasa'],'media_type':'image'},timeout=60).json()['collection']['items'];assert items,k
  item=items[0];assets=requests.get(item['href'],timeout=60).json();urls=assets if isinstance(assets,list)else[x['href']for x in assets['collection']['items']];d['url']=next((u for u in urls if '~medium.jpg'in u),next(u for u in urls if u.lower().endswith('.jpg')));d['source']='https://images.nasa.gov/details/'+d['nasa'];d['description']=item['data'][0].get('description','');d['title']=item['data'][0]['title']
 r=requests.get(d['url'],timeout=90);r.raise_for_status();im=Image.open(io.BytesIO(r.content)).convert('RGB');d['originalSize']=im.size;im.thumbnail((1400,1400),Image.Resampling.LANCZOS);im.save(ROOT/f'public/photos/{k}.webp',quality=88);print(k,im.size,d.get('title',''),flush=True)
 return k,d
out={}
for k,v in concurrent.futures.ThreadPoolExecutor(5).map(one,S.items()):out[k]=v
(ROOT/'art-source/expansion-photo-metadata.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
sheet=Image.new('RGB',(1000,600),'#0b1428');draw=ImageDraw.Draw(sheet)
for i,k in enumerate(out):
 im=Image.open(ROOT/f'public/photos/{k}.webp');im.thumbnail((180,155));x=i%5*200+(200-im.width)//2;y=i//5*200;sheet.paste(im,(x,y));draw.text((i%5*200+8,y+160),k,fill='white')
(ROOT/'artifacts').mkdir(exist_ok=True);sheet.save(ROOT/'artifacts/expansion-contact.jpg')
