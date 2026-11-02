# Agent instructions — construction timelapse

You run this whole project for the user. They should only answer your questions and approve the points below. Never ask them to copy, paste, edit files or run commands.

## When the user asks for a video

Treat any request like "make me a construction video" or "make me another one" as the start of a new project in a new `projects/` folder. Never overwrite or reuse an earlier project's files.

If the user says "continue", resume the most recent unfinished project instead. An unfinished manifest does not override an explicit request for a new video. Read its manifest, reuse every finished image and clip, and skip the questions they already answered.

### 1. Always ask the initial questions for a new video

Every request for a NEW construction video must begin with these questions in one short numbered message, then wait for the user's answers before generation:

1. Where is it? (beachfront, mountain, city lot, riverside, etc.)
2. What does the site look like at the start? (old house, empty lot, trash, etc.)
3. What should the finished house look like? Include storey count, style, materials and colors.
4. Pool or special features? (pool location, rooftop deck, helipad, helicopter, etc.)
5. What surroundings must remain unchanged?
6. Portrait 9:16 or landscape 16:9? (default: portrait)

If the opening request already answers some questions, list those answers briefly and ask only the remaining questions. If all are answered, ask a single brief confirmation of that initial brief and wait. Offer “surprise me” for creative choices. Never skip this initial exchange using saved preferences or an inferred brief. Every new project needs fresh answers from this initial exchange; never carry creative answers over from a previous video. When explicitly continuing the same project, use its production manifest to avoid repeating work.

State once alongside the questions: the standard run uses six images and five transitions, expected 10 Flow credits each, maximum 50 existing credits and no purchases. These are Flow credits, not chat tokens. The standing budget remains authorized; do not add a separate credit-approval pause or require approval of the finished-house image unless requested. After the initial answers, proceed through routine work automatically. This questionnaire is the only planned typed input: do not request another brief, prompt, file edit, command, or routine confirmation. Make reasonable choices for optional details the user leaves open. Ask again only for a genuinely new requirement or blocker, using a concise accept/decline or choice where possible. Approval is never a substitute for missing login or an actual listening review.

This authorization covers routine image creation, uploads, prompt entry, rendering, downloads, local assembly and corrections within the same 50-credit total. Failed jobs or retries do not create an extra budget. A request to create a video does not authorize purchases, subscriptions or account switching.

### 2. Set up, without bothering the user

- Create `projects/<short-project-name>/` in this folder and work only there.
- Check that Python 3 and FFmpeg are available. If one is missing, install it with the system's normal package manager. Ask the user only if installing needs their permission or password.
- Open Google Flow (https://labs.google/flow; it may redirect to flow.google.com) in your browser. If it isn't signed in, ask the user to sign in to their Google account in that browser window, and wait. Never ask for or type passwords.

### 3. Run WORKFLOW.md end to end

Follow `WORKFLOW.md` exactly: manifest, finished house first, six images with your built-in image generator, five Flow clips in Frames mode, sound and picture review, then `assemble.py`. Keep natural construction sounds; no music, singing, narration or dialogue. Flow audio must never enter the final video. Prepare five separate music-free scene-effect tracks and obtain actual listening review with hashes/rights before assembly. If you cannot listen, do not approve audio or hand over a final video as finished; save status `audio_review_pending` and request a reviewer. See WORKFLOW.md and audio-review.example.json.

Lock the finished house's storey count, floor elevations and roof height across all images and clips. Use WORKFLOW.md's architecture block in every Flow prompt. For two storeys, never build a temporary third floor. Inspect every clip at least once per second; extra floors appearing and disappearing fail visual review even if the ending is correct. Regenerate only within the remaining credit budget, otherwise report the blocker.

### 4. Stop only for a real blocker

- Missing login, unavailable tools, insufficient credits, a changed price/settings combination, or a correction that would exceed the 50-credit cap. Save progress and ask only for the decision needed.
- A new legal/upload-rights notice when applicable browser or platform rules require explicit approval. Reuse an approval already given for that account and notice; do not ask again without a material change.
- Required listening review if no capable listener is available. Never fabricate audio approval or bypass the music safeguards.

Do not ask “shall I continue?”, re-confirm the standard 50-credit run, or stop for routine intermediate image reviews. State the planned budget once as a progress update. When Flow's visible settings show the expected 10-credit cost, proceed; do not research pricing, inspect subscription pages, or poll balances between every clip. If the visible price differs or is unclear, resolve it before submitting.

All SOUND instructions pasted into Flow must be entirely ALL CAPS, including phase-specific additions. Use the canonical SOUND block in WORKFLOW.md. Exclude TV-like static, buzzing and distorted audio as well as music.

### Fast browser entry

Prepare and save all five complete prompts before opening the composer. Enter each prompt using one supported `fill` or clipboard-paste operation; do not simulate typing character by character. Use typing only when the editor does not support direct fill/paste. Read back the entered text once before submission. Upload the six assets once, reuse them for each endpoint pair, and submit each job once. Queue independent jobs when the UI supports it, record job IDs immediately, and use bounded waits instead of repeated checks.

For a trusted local checkout, users may optionally enable the app's file, browser and command permissions (or full access) to reduce tool prompts. Explain that these permissions do not provide Google sign-in, credits or legal consent. Never enable broad permissions yourself, suggest disabling safety controls, or make full access a requirement if narrower permissions suffice.

### 5. Hand over

When the final video passes the checks in `WORKFLOW.md`, reply with:

- The actual exported MP4 embedded/attached in the final chat response, plus a download link to that same file. In Codex desktop use `![Final construction video](/absolute/path/to/final.mp4)`. Use the real absolute path. An HTML preview, screenshot, folder or Flow link does not satisfy delivery. If the client cannot attach video, provide the actual MP4 download link and explain that limitation.
- Length, format, and credits used
- One line: "Want any clip changed? Tell me which one and what."

If they ask for a change, redo only that clip (within the remaining authorized budget; ask only if additional credits are needed), then assemble a new final video under a new filename.
