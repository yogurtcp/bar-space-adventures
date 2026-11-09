# Version 1.1: unified orbital map

- **180 layout checks passed:** one map, all 17 objects and their full labels accessible, eight orbital paths, no page scrolling, and all bilingual photo pop-ups fit at the ten viewport sizes listed below. Planet images and label centers are checked against overlaid controls so nothing is hidden by the map toolbar.
- Independent audio transcription confirmed the old Sun recording said “Sunday” and the replacement says “The Sun is a star…”. See `AUDIO_VERIFICATION.md`.
- **69 functional browser checks passed:** one shared map with no zone tabs, Sun-centered orbit paths, zoom/pan/fit, all 17 bilingual recording sequences, real photo loading, independent replay, cancellation, offline media, saved camera position and a safe automatic upgrade.
- Six Node tests cover content, real assets, save recovery, the Sun text regression and migration of old discoveries/settings into the unified map.

## Original release verification · 9 November 2026

- Four Node tests verify all eight planets are classified separately from the Sun, Moon, dwarf planet and small bodies; all 17 destinations have bilingual names/facts, real local photos, pixel art, both recordings and primary sources; saved progress restores safely; corrupt saves recover.
- **190 browser layout checks:** both maps and all 17 complete bilingual photo pop-ups fit without scrolling at 1366×900, 1024×768, 1180×820, 1280×800, 768×1024, 800×1280, 1024×600, 390×844, 320×640 and 900×414. Checks verify each full label fits its button, every target is reachable, pop-up content is contained and neither language's fact text overflows its own panel. Screenshots include the main maps and Saturn/Orion close-ups.
- Original map atlas and photo contact sheet inspected visually. Clipped ring artwork replaced using a separately generated atlas. Photo curation explicitly replaced an unrelated asteroid archive hit and an Orion 3D visualization with an actual Bennu spacecraft mosaic and a Hubble/Spitzer observational composite. Venus/Uranus use reviewed single-planet views. Processed colors and source credits are labeled.
- **65 functional browser checks passed.** Functional browser QA exercises English→Hebrew recorded name/fact sequences for every destination; independent replay, cancellation and stop; image enlargement; all discoveries; save restoration; install instructions; offline photos and audio; all 34 audio files decoding; a real second service-worker release that waits for an active picture to close, then reloads automatically while preserving progress and settings.
- Physical OS installation and native-speaker listening review were not performed. Voices are synthetic. This game stores progress locally, not in a cloud account.

Repeat with `npm test`, `npm run build`, `npm start`, then `node scripts/check-layout.mjs` and `node scripts/browser-check.mjs`. Browser QA uses disposable storage, leaves family saves untouched and restores its temporary upgrade release.
