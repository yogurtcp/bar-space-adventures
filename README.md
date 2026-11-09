# Bar in Space · בר בחלל 🚀

**[Play and install](https://yogurtcp.github.io/bar-space-adventures/)** · **[GitHub](https://github.com/yogurtcp/bar-space-adventures)**

A simple, tablet-first space explorer for Bar. Tap original **pixel-art** objects to open large **real spacecraft/telescope photographs**. Each of the **17 destinations** has its name and one short interesting sentence **written and spoken in English and Hebrew**. Opening an object automatically plays the English name and fact, then the Hebrew name and fact. Replay either language independently or both, stop narration, move between objects, or tap the photograph to enlarge it further.

There are two maps:

- **Solar system:** Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Moon, Pluto, asteroid Bennu and comet 67P. The eight planets are numbered in order from the Sun. The Moon, Pluto, asteroid and comet have separate type labels and a dashed border; they are not counted as planets.
- **Deep space:** stars (Pleiades), a nebula (Orion), the Milky Way photographed from inside our galaxy, and another galaxy (Andromeda).

The layout fills landscape and portrait tablets without scrolling. Both translations remain visible in the photo pop-up. Small phones use a compact board. The illustrations show representative objects; sizes, spacing and locations are not to scale. There are no mini-games, timers or accounts. Discoveries and settings stay on this device.

## Photographs and science

Every close-up comes from an actual observation, rather than generated art or a 3D visualization. Some are mosaics, enhanced-color images, or telescope observations of infrared/ultraviolet light represented in visible colors. Each photo has a description, credit and original source link; a large-view control preserves the whole image without cropping. All sources and image-specific attribution/license details are in [CREDITS.md](CREDITS.md). Original archive descriptions and download URLs are retained in [art-source/photo-metadata.json](art-source/photo-metadata.json).

Facts are child-friendly paraphrases from NASA Science. Each object links to its fact source in the help dialog and [src/objects.js](src/objects.js). Pluto is a dwarf planet. A star makes its own light; our Moon reflects sunlight. The photo of the Milky Way is a view from within it, not an imagined outside photograph.

## Install, offline and updates

Use **התקנה**. Chrome/Edge show a native installation prompt when available; otherwise device-specific instructions appear. Safari on iPad/iPhone: Share → Add to Home Screen. Installed mode hides the install action. OS/browser support determines installation availability.

The first complete download caches the entire app, all 17 photographs, pixel sprites and **34 name-and-fact recordings** (17 in each language). The footer confirms readiness. After that, exploration, photos and speech work offline. No external fonts, runtime speech API or analytics are used.

Online startups check for a newer published version. There is no recurring, focus, visibility or reconnection update polling. An incomplete release never replaces a complete cached version. An open picture or active recording defers activation until a safe boundary; closing the picture allows an automatic reload. Discovered objects, last destination, map zone and mute setting survive upgrades. Apps cannot fetch updates while closed.

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

The layout script checks both maps and all 17 written bilingual pop-ups at ten desktop/tablet/phone sizes. The functional script exercises all recordings, photos, replay, stop, photo zoom, save restoration, installation instructions, offline use and a real atomic service-worker upgrade. It uses disposable browser storage, temporarily builds a second release, and restores the original afterward. Screenshots/logs belong in ignored `artifacts/`. Physical OS installation requires a device check.

Push source to `main`, then `npm run deploy` to test/build, publish `dist/` to `gh-pages` and configure GitHub Pages with authenticated GitHub CLI.

## Rebuild assets

- **Pixel art:** made with the built-in imagegen tool. Original atlases and exact prompts: [art-source/PROMPTS.md](art-source/PROMPTS.md). `python3 scripts/prepare-art.py` extracts transparent sprites and creates padded PNG install icons; requires Pillow. The ring atlas corrects clipped Saturn rings in the first atlas.
- **Photographs:** `python3 scripts/download-photos.py` downloads NASA archive assets and automatically applies the reviewed replacements in `curate-photos.py`. Requires requests and Pillow. `src/photo-sources.js` contains the curated bilingual caption and attribution for each. Generated illustrations and real photos are stored separately.
- **English:** build-time Aria synthetic voice, `edge-tts==7.3.1`. Run `python scripts/generate-english.py` in an environment containing edge-tts. Recordings are bundled MP3 files.
- **Hebrew:** local female BlueTTS 2.5 voice, matching the other Bar games, with explicit pronunciation strings for every complete name-and-fact sentence. Settings, phonemes and audio statistics: [scripts/hebrew/blue-recordings.json](scripts/hebrew/blue-recordings.json). Run `generate-hebrew-blue.py --engine-path ... --model-dir ... --g2p-model ...` with `requirements-hebrew-blue.txt`. The app has its own synthesis cache at `~/.cache/bar-space-hebrew-v1`. [Engine license](scripts/hebrew/BLUETTS_LICENSE.txt). Recordings are synthetic; no family photo is published.
