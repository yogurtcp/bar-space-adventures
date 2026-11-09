# Sun pronunciation correction

The isolated text `Sun.` was interpreted by the English voice engine as the weekday abbreviation. The original recording was independently transcribed using faster-whisper `tiny.en` on CPU:

> Sunday. The Sun is a star that gives Earth light and warmth.

The replacement at `public/audio/en/sun-v2.mp3` uses the complete astronomical sentence without the abbreviation-like prefix. Its independent transcription was:

> The Sun is a star that gives Earth light and warmth.

The written fact is identical to the replacement speech. Hebrew narration is unchanged. The old `public/audio/en/01.mp3` is removed, and the app/build now use the explicit `audioEn` path for each object. This ensures installed copies download the corrected file as part of the atomic startup update.

Review transcript: `artifacts/sun-audio-review.json` (local, ignored). ASR is an automated check, not a substitute for a human listening review.
