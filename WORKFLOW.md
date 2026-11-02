# Construction transformation — Codex or Claude

## Required result

Create a construction timelapse ending on a fully finished house or resort. **Keep natural construction sounds. Exclude background music, singing, narration and dialogue.** Preserve any surroundings the user specifies. Do not default to silent video.

Use an available image-generation/editing backend, authenticated Google Flow browser access, local files, Python 3 and FFmpeg. Codex may use its built-in image generator; Claude needs an available image backend or supplied keyframes. The same assets and instructions work with either agent; browser tool calls differ. Do not assume access to a free hosted image API.

## 1. Record the brief

Save a project manifest containing:
- Setting, before condition, finished house design and pool location if applicable.
- Aspect ratio: 9:16 portrait or 16:9 landscape. Choose before generating images.
- Fixed camera and background areas that must remain unchanged.
- Architecture lock: final storey count, floor elevations, maximum roof height, footprint, roof form and major openings. Explicitly distinguish a rooftop deck, railing or helipad from an additional enclosed storey.
- Audio mode: `construction_sfx_no_music`.
- Selected Flow account, existing-credit cap and cash budget; cash defaults to zero.
- Ordered assets, exact prompts, submitted jobs, downloaded clips and current status.

Reuse completed work when resuming. Standard-run authorization is 50 existing Flow credits, five transitions at 10 credits each, with zero cash spending. Use portrait 9:16 unless the brief says otherwise. Confirm the selected account and expected settings from the visible UI once; no separate pricing research or repeated credit-approval prompts. Never change accounts, buy credits or exceed the agreed budget without authorization. Handle agreements under the agent's applicable confirmation rules.

## 2. Create six images, starting with the ending

Generate **06 completed house first**, review it yourself and continue without a user approval pause unless a preview was requested. Require finished roof, facade, windows, doors, paths, landscaping and furnishings. If requested, the pool is fully tiled, filled with clean water and surrounded by a finished deck. No workers, scaffolding, tools, materials or unfinished patches. Keep the whole house and pool in frame.

Use that image to fix the camera, property outline, architecture and pool position. Derive the other stages:
1. Original lot / before condition.
2. Cleanup and grading.
3. Foundations and pool basin, if applicable.
4. Structural shell.
5. Exterior and grounds finishing.
6. Completed house.

Lock the final design before deriving stages. For a two-storey design, every structural and finishing image must show only the ground floor and one upper floor; earlier stages may contain fewer completed floors, never more. Match floor elevations and roof height to image 06. Do not add temporary floors, stacked rooms, rooftop apartments or extra slabs above the final roof. Scaffolding must be visually distinct from permanent construction. Reject inconsistent keyframes before spending credits.

Use the previous stage plus the completed reference where supported. Change only the work area. Check all six images for camera, footprint and background consistency before spending video credits. Correct major geometry changes; minor texture differences alone do not require regeneration.

## 3. Animate five adjacent pairs in Flow

Upload the six images once. Use **Frames**, the chosen aspect ratio, one output per job, and an economical model supporting both endpoints. Our tested setting was Veo 3.1 Lite, 720p, 8 seconds, 10 credits per output; use this preset and read its visible cost once when configuring the project. Proceed under the standing 50-credit authorization if it shows 10 per output. If the cost differs or is unclear, resolve that before spending; never assume pricing cannot change.

Submit exactly five pairs: **01→02, 02→03, 03→04, 04→05, 05→06**. Each prompt combines a short phase-specific action with this common instruction. Keep the entire SOUND block and any phase-specific sound instructions in ALL CAPS, including the ending instruction:

> Fixed camera matching the supplied start and end frames. No pan, tilt, zoom, shake, cuts or reframing. Preserve the property footprint, house geometry and specified surroundings. Show only the workers, tools and activity needed for this construction phase, with continuous plausible accelerated work. No unrelated objects, vehicles, people, text or subtitles. **SOUND: NATURAL, SCENE-MATCHED CONSTRUCTION SOUNDS ONLY: TOOLS, MACHINERY, FOOTSTEPS, MATERIAL HANDLING, AND WATER WHERE VISIBLY APPROPRIATE. INCLUDE HELICOPTER ROTOR SOUND ONLY WHEN A HELICOPTER IS PRESENT. NO BACKGROUND MUSIC, MUSICAL SCORE, SOUNDTRACK, BEAT, SINGING, NARRATION, VOICEOVER, OR DIALOGUE. NO TV STATIC, RADIO INTERFERENCE, ELECTRONIC BUZZING, GLITCH NOISE, HARSH HISS, CRACKLING, CLIPPING, OR DISTORTED AUDIO. KEEP EFFECTS CLEAR, NATURAL, AND SYNCHRONIZED WITH VISIBLE ACTION. DO NOT ADD MUSIC AT ANY POINT.** End exactly on the supplied endpoint.

Append this architecture instruction to **every** clip, replacing placeholders from the manifest:

> ARCHITECTURE LOCK: THE FINISHED HOUSE HAS EXACTLY {STOREY_COUNT} STOREYS: {FLOOR_DESCRIPTION}. USE THE SAME FOOTPRINT, FLOOR ELEVATIONS AND MAXIMUM ROOF HEIGHT AS THE COMPLETED REFERENCE. NEVER CONSTRUCT AN EXTRA STOREY, TEMPORARY FLOOR, ROOFTOP ROOM OR ADDITIONAL ROOF SLAB. BUILD ONLY THE STRUCTURE NEEDED FOR THIS PHASE, PROGRESSING TOWARD THE END FRAME. NO FLOOR MAY APPEAR AND THEN BE DEMOLISHED, SHRINK, MELT OR DISAPPEAR TO MATCH THE ENDING. A ROOFTOP DECK OR HELIPAD IS NOT AN EXTRA ENCLOSED STOREY.

For two storeys use `STOREY_COUNT = TWO` and `FLOOR_DESCRIPTION = GROUND FLOOR PLUS ONE UPPER FLOOR`. Do not infer extra floors from tall scaffolding. Phase actions must name the allowed work, e.g. “install the roof directly above the existing upper floor,” rather than a vague “keep building upward.”

Add to the final clip:

> Complete all work before the ending. Remove every worker, scaffold, tool, bucket, material stack and piece of debris from the property. Finish the pool, deck, landscaping and furnishings. Final two seconds show only the fully completed property. SOUND: CONSTRUCTION SOUNDS SUBSIDE AS WORK ENDS. KEEP ONLY APPROPRIATE NATURAL AMBIENCE. NO MUSIC, SPEECH, STATIC, BUZZING, OR DISTORTION.

Save all five prompts in the project first. Enter each complete prompt with one supported fill/paste operation, not character-by-character typing; read it back once. Upload assets once and reuse them. Queue independent jobs if supported without duplicating submissions. Record each submission once. Do not repeat Generate while a job is pending. Download original completed clips. Stop on exhausted credits; do not buy more or silently change the agreed settings.

## 4. Build a separate music-free sound layer

**Never use Flow's audio in the deliverable.** It can contain music even when the prompt forbids it. Flow supplies visuals only; strengthening the prompt or checking that an audio stream exists does not solve this.

Prepare five separate scene-effect tracks: demolition/tools, assembly, finishing, water, footsteps, and any explicitly requested helicopter or machinery. Use owned or appropriately licensed recordings, or isolated SFX generated without music. Never add a music bed. Avoid recurring melodic or beat-like loops.

Listen to every SFX track against its corresponding clip. Confirm no music, singing, speech, TV-like static, electronic buzzing, clipping, distortion or unrelated sounds, and record usage rights. If the agent cannot listen, it must not mark the review as passed: request listening review or stop with status `audio_review_pending`. Speech recognition, metadata, a successful decode or a music classifier alone is not listening approval. Do not mute the video and call that fixed.

Copy `audio-review.example.json` into the project. After actual listening, fill in the reviewer, the SHA-256 of each source clip and SFX file, rights, and the three pass flags. Review covers all five pairs in order; changed files invalidate it. Use `shasum -a 256 <file>` to obtain a hash. Never copy pass flags from another project or approve unplayed audio.

Inspect a contact sheet sampled at least once per second across every clip, plus its opening and ending. Count visible storeys and compare floor lines and roof height with image 06; inspect suspect intervals more closely. A correct endpoint does not excuse a temporary third storey. Reject any clip that adds and removes floors, exceeds the final building height, or contains major geometry changes or unrelated objects. Do not hide the error with a final still. Regenerate only the affected clip within the remaining credit cap; if there is no budget, save status `visual_review_failed` and report the blocker instead of claiming completion. Registered reference overlays may fix protected static backgrounds, but must stay outside the work area. Preserve the separately approved SFX in every visual correction; never remap Flow audio back into the final file.

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
- Storey count and architecture remain within the final design throughout every clip; no extra floor appears and disappears.
- Completed final frame matches image 06, with no remaining construction work.
- Required surroundings preserved; no unrelated generated content.
- Full video decode succeeds and the audio stream exists.

Save final MP4, six images, five original clips, exact prompts, manifest, Flow link and actual credits used. Report material remaining defects. Account usage percentages, if recorded, are rounded account-wide readings rather than precise project token counts.

## 6. Deliver the actual export in chat

After acceptance checks pass, export the actual final MP4 and embed/attach that video in the final chat response. In Codex desktop use `![Final construction video](/absolute/path/to/final.mp4)` with the real absolute file path, and include a download link to the same MP4. In another client use its supported native video attachment. An HTML player, preview page, storyboard, screenshot, folder opening or Flow project link is not the final deliverable. Do not stop at an HTML preview before export. If the client cannot attach or play video, provide the actual MP4 download link and state that limitation. Never label an unreviewed draft as final.
