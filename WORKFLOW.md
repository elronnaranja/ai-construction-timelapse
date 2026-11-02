# Construction transformation — Codex or Claude

## Required result

Create a construction timelapse ending on a fully finished house or resort. **Keep natural construction sounds. Exclude background music, singing, narration and dialogue.** Preserve any surroundings the user specifies. Do not default to silent video.

Use an available image-generation/editing backend, authenticated Google Flow browser access, local files, Python 3 and FFmpeg. Codex may use its built-in image generator; Claude needs an available image backend or supplied keyframes. The same assets and instructions work with either agent; browser tool calls differ. Do not assume access to a free hosted image API.

## 1. Record the brief

Save a project manifest containing:
- Setting, before condition, finished house design and pool location if applicable.
- Aspect ratio: 9:16 portrait or 16:9 landscape. Choose before generating images.
- Fixed camera and background areas that must remain unchanged.
- Audio mode: `construction_sfx_no_music`.
- Selected Flow account, existing-credit cap and cash budget; cash defaults to zero.
- Ordered assets, exact prompts, submitted jobs, downloaded clips and current status.

Reuse completed work when resuming. Confirm the visible account and current credit costs. Never change accounts, buy credits or exceed the agreed budget without authorization. Handle agreements under the agent's applicable confirmation rules.

## 2. Create six images, starting with the ending

Generate **06 completed house first**. Require finished roof, facade, windows, doors, paths, landscaping and furnishings. If requested, the pool is fully tiled, filled with clean water and surrounded by a finished deck. No workers, scaffolding, tools, materials or unfinished patches. Keep the whole house and pool in frame.

Use that image to fix the camera, property outline, architecture and pool position. Derive the other stages:
1. Original lot / before condition.
2. Cleanup and grading.
3. Foundations and pool basin, if applicable.
4. Structural shell.
5. Exterior and grounds finishing.
6. Approved completed house.

Use the previous stage plus the completed reference where supported. Change only the work area. Check all six images for camera, footprint and background consistency before spending video credits. Correct major geometry changes; minor texture differences alone do not require regeneration.

## 3. Animate five adjacent pairs in Flow

Upload the six images once. Use **Frames**, the chosen aspect ratio, one output per job, and an economical model supporting both endpoints. Our tested setting was Veo 3.1 Lite, 720p, 8 seconds, 10 credits per output; verify the live settings and cost every run.

Submit exactly five pairs: **01→02, 02→03, 03→04, 04→05, 05→06**. Each prompt combines a short phase-specific action with this common instruction:

> Fixed camera matching the supplied start and end frames. No pan, tilt, zoom, shake, cuts or reframing. Preserve the property footprint, house geometry and specified surroundings. Show only the workers, tools and activity needed for this construction phase, with continuous plausible accelerated work. No unrelated objects, vehicles, people, text or subtitles. **AUDIO: natural construction sounds only—tools, machinery, footsteps, material handling and water where visibly appropriate. NO background music, musical score, soundtrack, beat, singing, narration, voiceover or dialogue. Do not add music at any point.** End exactly on the supplied endpoint.

Add to the final clip:

> Complete all work before the ending. Remove every worker, scaffold, tool, bucket, material stack and piece of debris from the property. Finish the pool, deck, landscaping and furnishings. Final two seconds show only the fully completed property. Construction sounds subside as work ends; no music or speech.

Record each submission once. Do not repeat Generate while a job is pending. Download original completed clips. Stop on exhausted credits; do not buy more or silently change the agreed settings.

## 4. Build a separate music-free sound layer

**Never use Flow's audio in the deliverable.** It can contain music even when the prompt forbids it. Flow supplies visuals only; strengthening the prompt or checking that an audio stream exists does not solve this.

Prepare five separate scene-effect tracks: demolition/tools, assembly, finishing, water, footsteps, and any explicitly requested helicopter or machinery. Use owned or appropriately licensed recordings, or isolated SFX generated without music. Never add a music bed. Avoid recurring melodic or beat-like loops.

Listen to every SFX track against its corresponding clip. Confirm no music, singing, speech or unrelated sounds, and record usage rights. If the agent cannot listen, it must not mark the review as passed: request listening review or stop with status `audio_review_pending`. Speech recognition, metadata, a successful decode or a music classifier alone is not listening approval. Do not mute the video and call that fixed.

Copy `audio-review.example.json` into the project. After actual listening, fill in the reviewer, the SHA-256 of each source clip and SFX file, rights, and the three pass flags. Review covers all five pairs in order; changed files invalidate it. Use `shasum -a 256 <file>` to obtain a hash. Never copy pass flags from another project or approve unplayed audio.

Check each clip's opening, middle and ending for unrelated objects, major geometry changes or unfinished work. Registered reference overlays may fix protected static backgrounds, but must stay outside the work area. Preserve the separately approved SFX in every visual correction; never remap Flow audio back into the final file.

## 5. Assemble and verify

Run after listening approval:

```sh
python3 assemble.py --clips clip01.mp4 clip02.mp4 clip03.mp4 clip04.mp4 clip05.mp4 \
  --sfx-tracks sfx01.wav sfx02.wav sfx03.wav sfx04.wav sfx05.wav \
  --audio-review audio-review.json --hero 06-completed.png \
  --output final.mp4 --aspect 9:16
```

The assembler always ignores Flow audio. It uses only the five separate reviewed SFX tracks, normalizes frame rate and geometry, fades effects at the ending, and adds a two-second completed-image hold. Missing or failed review, missing effects, or changed clip/SFX hashes block rendering. There is no raw-Flow-audio fallback. Keep SFX and the review file with the project when handing off between Codex and Claude.

Listen to the assembled final too, including joins and the ending. Do not deliver a file as music-free until it passes. This is a delivery safeguard, not a guarantee that Flow will stop generating music or that a false human review can be detected automatically.

Acceptance checks:
- Correct aspect ratio; full house and pool visible without stretching.
- Separate reviewed construction effects present; no audible music or speech; Flow audio excluded.
- Completed final frame matches image 06, with no remaining construction work.
- Required surroundings preserved; no unrelated generated content.
- Full video decode succeeds and the audio stream exists.

Save final MP4, six images, five original clips, exact prompts, manifest, Flow link and actual credits used. Report material remaining defects. Account usage percentages, if recorded, are rounded account-wide readings rather than precise project token counts.
