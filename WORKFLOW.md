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

## 4. Review sound and picture

**Listen to every clip.** Confirm construction sounds are present and relevant, and no music, singing, narration or dialogue is audible. Prompts cannot guarantee this. Speech detection alone does not verify absence of music.

If a clip contains music, preserve the good construction audio elsewhere. Replace only the affected segment with reviewed, appropriately licensed construction effects, use an available separation tool and listen for artifacts, or regenerate within the approved budget. Do not mute the entire video as a shortcut. If a satisfactory repair is unavailable, report the specific clip and leave it pending.

Check each clip's opening, middle and ending. Reject unrelated objects, major geometry changes or an unfinished final property. For protected static backgrounds, a registered reference overlay can remove artifacts without rerendering; keep it outside the work area and inspect for seams. **Retain the audio when applying visual fixes.** Project-specific masks must be measured again for each scene.

## 5. Assemble and verify

After audio review, run `assemble.py --clips <five ordered clips> --hero <approved image 06> --output <new MP4> --aspect 9:16` (or 16:9).

The script retains and normalizes existing audio, handles clips without audio, fades the final construction sounds, and adds a two-second finished-image hold. It does **not** remove music; do the audio review first. Never use the legacy silent assembler for normal delivery.

Acceptance checks:
- Correct aspect ratio; full house and pool visible without stretching.
- Relevant construction effects retained; no audible music or speech.
- Completed final frame matches image 06, with no remaining construction work.
- Required surroundings preserved; no unrelated generated content.
- Full video decode succeeds and the audio stream exists.

Save final MP4, six images, five original clips, exact prompts, manifest, Flow link and actual credits used. Report material remaining defects. Account usage percentages, if recorded, are rounded account-wide readings rather than precise project token counts.
