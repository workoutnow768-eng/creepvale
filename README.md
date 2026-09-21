creepvale

Fully autonomous daily video pipeline for the @creepvale Horror/Spooky account. Sister repo to dark-fantasy, pallowyn, chromeage, voidcrete and vaporune -- same architecture (Higgsfield still -> Minimax Hailuo 2.3 animate -> ffmpeg music mux -> Buffer GraphQL schedule), but an atmospheric-dread horror visual identity (not gore, not jump-scares). See CREEPVALE_VIDEO_STYLE.md for the full style lock.

## What one run does

1. Generate (`scripts/main.py generate`): picks the next scene(s) from `scripts/scene_bank.py`'s rotation, for each one:
   - generates a still image (Higgsfield Soul v2, 1080p, 9:16)
   - animates it into a 6s silent video (Minimax Hailuo 2.3)
   - downloads the music track and detects its real duration via ffprobe
   - mixes in the music (ffmpeg, fading in/out, stepping through the track so consecutive posts don't reuse the same slice)
   - writes a manifest of the finished .mp4 paths + scheduled times
2. Commit + push those .mp4 files (Buffer needs a public URL to fetch from).
3. Schedule (`scripts/main.py schedule`): reads the manifest, creates one Buffer post per video per channel, then updates the rotation state and removes the manifest.

Runs daily at 17:35 UTC via the scheduled workflow, or on demand from the Actions tab.

## One-time setup checklist

- [x] Repo is public (required for raw.githubusercontent.com fetches)
- [ ] `HIGGSFIELD_API_KEY` secret set
- [ ] `MUSIC_TRACK_URL` secret set (a horror-appropriate track -- do NOT reuse pallowyn's "Carnival of the Macabre.mp3", wrong tone; see CREEPVALE_VIDEO_STYLE.md)
- [ ] `BUFFER_API` secret set
- [ ] Confirm which Buffer channel/account this niche actually posts to (naming was ambiguous between "creepvale" and "creelatin" in earlier planning -- resolve before the first live run)
- [ ] Confirm Instagram/YouTube channels are connected in Buffer if used
- [ ] Test with a manual run from the Actions tab before relying on the schedule

## Rotation state

`state/creepvale_state.json` tracks which scene is next (`last_scene_index`), the next open posting slot (`scheduled_up_to`), and where in the music track the next mux should start (`music_offset_seconds`). The bot owns these fields -- don't hand-edit them while the scheduled workflow is active.

`posts_per_day` starts at 1 for the first test run (same testing process pallowyn and dark-fantasy went through) -- bump to 3 once a run succeeds end-to-end.

