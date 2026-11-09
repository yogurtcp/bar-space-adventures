"""Build-time English voice. Requires edge-tts==7.3.1. No runtime speech service."""
import asyncio,json,pathlib,subprocess
import edge_tts
ROOT=pathlib.Path(__file__).resolve().parents[1]
async def main():
 objects=json.loads(subprocess.check_output(['node','--input-type=module','-e',"import {objects} from './src/objects.js';console.log(JSON.stringify(objects))"],cwd=ROOT))
 sem=asyncio.Semaphore(4)
 async def one(o):
  dest=ROOT/'public'/o['audioEn'];dest.parent.mkdir(parents=True,exist_ok=True)
  async with sem:
   if not dest.exists():
    for attempt in range(4):
     try:
      await edge_tts.Communicate(o['speechEn'],'en-US-AriaNeural',rate='-12%').save(str(dest));break
     except Exception:
      if attempt==3:raise
      await asyncio.sleep(2)
   print(o['id'],o['speechEn'],flush=True)
 await asyncio.gather(*(one(o)for o in objects))
asyncio.run(main())
