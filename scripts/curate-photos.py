"""Apply reviewed NASA replacements. These are downloaded photographs, never generated images."""
from pathlib import Path
from PIL import Image,ImageDraw
import requests,io,json,concurrent.futures
ROOT=Path(__file__).resolve().parents[1]
replacements={
'asteroid':{'source':'https://science.nasa.gov/resource/bennu-mosaic/','download':'https://assets.science.nasa.gov/dynamicimage/assets/science/psd/solar/2023/09/b/bennu_dec10.jpg?w=1024&h=968&fit=clip&crop=faces%2Cfocalpoint','title':'Bennu Mosaic','creator':'NASA / Goddard / University of Arizona','description':'Mosaic of 12 OSIRIS-REx PolyCam photographs of asteroid Bennu, collected December 2, 2018.'},
'nebula':{'source':'https://svs.gsfc.nasa.gov/30775/','download':'https://svs.gsfc.nasa.gov/vis/a030000/a030700/a030775/orion_nebula_vis_ir-hst_sst-3240x3240_print.jpg','title':'Hubble and Spitzer Composite of the Orion Nebula','creator':'NASA / ESA / T. Megeath (U. Toledo) / M. Robberto (STScI)','description':'Real composite of Hubble visible-light and Spitzer infrared observations. Infrared light is represented by visible colors; not a 3D visualization.'},
'venus':{'source':'https://science.nasa.gov/venus/venus-facts/','download':'https://assets.science.nasa.gov/dynamicimage/assets/science/cds/general/images/2024/03/venus-mariner-10-pia23791-fig2.jpg?w=1096&h=1096&fit=clip&crop=faces%2Cfocalpoint','title':'Venus from Mariner 10, single processed view','creator':'NASA / JPL-Caltech','description':'Single newly processed Mariner 10 image of the cloudy globe of Venus.'},
'uranus':{'source':'https://science.nasa.gov/uranus/facts/','download':'https://assets.science.nasa.gov/dynamicimage/assets/science/cds/general/images/2024/03/uranus-pia18182-16x9-1.jpg?w=1920&h=1080&fit=clip&crop=faces%2Cfocalpoint','title':'Uranus from Voyager 2','creator':'NASA / JPL-Caltech','description':'Full pale blue globe of Uranus photographed by Voyager 2.'}}
def get(pair):
 k,v=pair;r=requests.get(v['download'],timeout=90);r.raise_for_status();im=Image.open(io.BytesIO(r.content)).convert('RGB');v['originalSize']=im.size;im.thumbnail((1400,1400));im.save(ROOT/f'public/photos/{k}.webp',quality=88);print(k,im.size,flush=True);return k,v
metadata=json.loads((ROOT/'art-source/photo-metadata.json').read_text())
for k,v in concurrent.futures.ThreadPoolExecutor(4).map(get,replacements.items()):metadata[k]=v
(ROOT/'art-source/photo-metadata.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2))
sheet=Image.new('RGB',(1000,760),'#0b1428');d=ImageDraw.Draw(sheet)
for i,key in enumerate(metadata):
 im=Image.open(ROOT/f'public/photos/{key}.webp');im.thumbnail((180,155));x=(i%5)*200+(200-im.width)//2;y=(i//5)*190;sheet.paste(im,(x,y));d.text(((i%5)*200+10,y+160),key,fill='white')
sheet.save(ROOT/'art-source/photo-contact.jpg')
