# Bar in Space · בר בחלל 🚀

**[Play and install](https://yogurtcp.github.io/bar-space-adventures/)** · **[GitHub](https://github.com/yogurtcp/bar-space-adventures)**

A simple, tablet-first space explorer for Bar. Tap original **pixel-art** objects to open large **real spacecraft/telescope photographs**. Each of the **17 destinations** has its name and one short interesting sentence **written and spoken in English and Hebrew**. Opening an object automatically plays the English name and fact, then the Hebrew name and fact. Replay either language independently or both, stop narration, move between objects, or tap the photograph to enlarge it further.

**Version 1.1 shows one continuous star map.** The Sun sits at the center of eight nested orbit paths, with each planet on its own orbit in the correct order. The Moon has a small orbit around Earth. Pluto, an asteroid, a comet, stars, the Orion Nebula, the Milky Way and Andromeda are all visible on this same canvas, without category tabs or tile panels. Drag to pan, use +/− to zoom, or choose **כל החלל / Show all** to fit everything. Tablet portrait and landscape have purpose-built sky-chart arrangements; narrow/short screens can pan and zoom within the same map.

The layout fills the tablet viewport without page scrolling. Both translations remain visible in each photo pop-up. The chart is illustrative: object sizes, orbital spacing, orientation and object locations are not to scale, and galaxies are vastly beyond the Solar System. Discoveries, camera position and settings stay on this device.

**Sun pronunciation fix:** the old isolated `Sun.` was expanded by the voice engine to “Sunday.” The replacement recording starts with the complete astronomical sentence, “The Sun is a star that gives Earth light and warmth.” Automatic speech recognition confirmed the old and new audio; see [AUDIO_VERIFICATION.md](AUDIO_VERIFICATION.md). The incorrect recording is removed from the published assets.

## Photographs and science

Every close-up comes from an actual observation, rather than generated art or a 3D visualization. Some are mosaics, enhanced-color images, or telescope observations of infrared/ultraviolet light represented in visible colors. Each photo has a description, credit and original source link; a large-view control preserves the whole image without cropping. All sources and image-specific attribution/license details are in [CREDITS.md](CREDITS.md). Original archive descriptions and download URLs are retained in [art-source/photo-metadata.json](art-source/photo-metadata.json).

Facts are child-friendly paraphrases from NASA Science. Each object links to its fact source in the help dialog and [src/objects.js](src/objects.js). Pluto is a dwarf planet. A star makes its own light; our Moon reflects sunlight. The photo of the Milky Way is a view from within it, not an imagined outside photograph.

## Install, offline and updates

Use **התקנה**. Chrome/Edge show a native installation prompt when available; otherwise device-specific instructions appear. Safari on iPad/iPhone: Share → Add to Home Screen. Installed mode hides the install action. OS/browser support determines installation availability.

The first complete download caches the entire app, all 17 photographs, pixel sprites and **34 name-and-fact recordings** (17 in each language). The footer confirms readiness. After that, exploration, photos and speech work offline. No external fonts, runtime speech API or analytics are used.

Online startups check for a newer published version. There is no recurring, focus, visibility or reconnection update polling. An incomplete release never replaces a complete cached version. An open picture or active recording defers activation until a safe boundary; closing the picture allows an automatic reload. Discovered objects, last destination, map position/zoom and mute setting survive upgrades. Existing saves from the old two-category layout keep their discoveries and sound settings. Apps cannot fetch updates while closed.

The app has its own manifest scope/ID, `bar-space-` cache prefix and `bar-space-v1` save key, isolated from the other Bar games. Saves do not sync across devices/profiles; clearing browser data removes them.

## Develop and publish

Node 18+:

```sh
npm ci
npm test
npm run build
npm start
```

Open http://127.0.0.1:4190. The app uses browser ES modules and CSS, with no runtime dependencies. Relative paths support both root hosting and `/bar-space-adventures/`.

With the preview server running and Chrome installed:

```sh
node scripts/check-layout.mjs
node scripts/browser-check.mjs
```

The layout script checks the unified map, all 17 reachable objects and labels, eight orbital paths and every bilingual pop-up at ten desktop/tablet/phone sizes. The functional script exercises all recordings, photos, map panning/zoom/fit, replay, stop, photo zoom, save restoration, installation instructions, offline use and a real atomic service-worker upgrade. It uses disposable browser storage, temporarily builds a second release, and restores the original afterward. Screenshots/logs belong in ignored `artifacts/`. Physical OS installation requires a device check.

Push source to `main`, then `npm run deploy` to test/build, publish `dist/` to `gh-pages` and configure GitHub Pages with authenticated GitHub CLI.

## Rebuild assets

- **Pixel art:** made with the built-in imagegen tool. Original atlases and exact prompts: [art-source/PROMPTS.md](art-source/PROMPTS.md). `python3 scripts/prepare-art.py` extracts transparent sprites and creates padded PNG install icons; requires Pillow. The ring atlas corrects clipped Saturn rings in the first atlas.
- **Photographs:** `python3 scripts/download-photos.py` downloads NASA archive assets and automatically applies the reviewed replacements in `curate-photos.py`. Requires requests and Pillow. `src/photo-sources.js` contains the curated bilingual caption and attribution for each. Generated illustrations and real photos are stored separately.
- **English:** build-time Aria synthetic voice, `edge-tts==7.3.1`. Run `python scripts/generate-english.py` in an environment containing edge-tts. Recordings are bundled MP3 files.
- **Hebrew:** local female BlueTTS 2.5 voice, matching the other Bar games, with explicit pronunciation strings for every complete name-and-fact sentence. Settings, phonemes and audio statistics: [scripts/hebrew/blue-recordings.json](scripts/hebrew/blue-recordings.json). Run `generate-hebrew-blue.py --engine-path ... --model-dir ... --g2p-model ...` with `requirements-hebrew-blue.txt`. The app has its own synthesis cache at `~/.cache/bar-space-hebrew-v1`. [Engine license](scripts/hebrew/BLUETTS_LICENSE.txt). Recordings are synthetic; no family photo is published.
