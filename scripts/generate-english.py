"""Build-time English voice. Requires edge-tts==7.3.1. No runtime speech service."""
import asyncio,json,pathlib,subprocess
import edge_tts
ROOT=pathlib.Path(__file__).resolve().parents[1]
async def main():
 texts=json.loads(subprocess.check_output(['node','scripts/audio-catalog.js'],cwd=ROOT))['en']
 sem=asyncio.Semaphore(4)
 async def one(i,text):
  dest=ROOT/f'public/audio/en/{i:02}.mp3';dest.parent.mkdir(parents=True,exist_ok=True)
  async with sem:
   if not dest.exists():
    for attempt in range(4):
     try:
      await edge_tts.Communicate(text,'en-US-AriaNeural',rate='-12%').save(str(dest));break
     except Exception:
      if attempt==3:raise
      await asyncio.sleep(2)
   print(i,text,flush=True)
 await asyncio.gather(*(one(i,t)for i,t in enumerate(texts,1)))
asyncio.run(main())
