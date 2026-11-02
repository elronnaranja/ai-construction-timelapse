# Agent instructions — construction timelapse

You run this whole project for the user. They should only answer your questions and approve the points below. Never ask them to copy, paste, edit files or run commands.

## When the user asks for a video

Treat any request like "make me a construction video" or "make me another one" as the start of a new project in a new `projects/` folder. Never overwrite or reuse an earlier project's files.

If the user says "continue" (or a project in `projects/` has an unfinished manifest), resume the most recent unfinished project instead. Read its manifest, reuse every finished image and clip, and skip the questions they already answered.

### 1. Ask the questions (one message, short)

Ask everything in one numbered list, with an example answer for each, then wait:

1. Where is it? (e.g. beachfront, mountain, city lot, riverside)
2. What does the lot look like now? (e.g. empty grass, old shack, overgrown jungle, littered lot)
3. What should the finished house look like? (style, floors, materials, colors)
4. Pool? (no / yes, and where)
5. What must stay the same around it? (e.g. neighbors, road, trees, the sea)
6. Vertical 9:16 for TikTok/Reels/Shorts, or horizontal 16:9 for YouTube?
7. How many Flow credits can I use at most? (one video is five clips; I'll check the live cost)

Tell them they can just say "surprise me" for 1–5. Then pick a strong idea yourself, or offer 8 short numbered ideas if they'd rather choose.

### 2. Set up, without bothering the user

- Create `projects/<short-project-name>/` in this folder and work only there.
- Check that Python 3 and FFmpeg are available. If one is missing, install it with the system's normal package manager. Ask the user only if installing needs their permission or password.
- Open Google Flow (https://labs.google/flow; it may redirect to flow.google.com) in your browser. If it isn't signed in, ask the user to sign in to their Google account in that browser window, and wait. Never ask for or type passwords.

### 3. Run WORKFLOW.md end to end

Follow `WORKFLOW.md` exactly: manifest, finished house first, six images with your built-in image generator, five Flow clips in Frames mode, sound and picture review, then `assemble.py`. Keep natural construction sounds; no music, singing, narration or dialogue. Flow audio must never enter the final video. Prepare five separate music-free scene-effect tracks and obtain actual listening review with hashes/rights before assembly. If you cannot listen, do not approve audio or hand over a final video as finished; save status `audio_review_pending` and request a reviewer. See WORKFLOW.md and audio-review.example.json.

### 4. The only times you stop

Ask the user a short yes/no question and wait:

1. **Image 06, the finished house.** Show it before making the other images. Redo it until they approve.
2. **Before you spend Flow credits.** Show the live cost per clip and the total for five clips, and wait for their OK. Stay inside their credit limit. Never buy credits, start a subscription or change accounts.
3. **Anything Flow asks you to accept** (upload notice, terms). Tell them what it says and wait for their OK.
4. **A problem you can't fix within the budget** (out of credits, a clip that keeps failing). Explain it in one or two sentences and ask what they want.

Everything else you decide and do yourself. Don't send progress questions like "shall I continue?".

### 5. Hand over

When the final video passes the checks in `WORKFLOW.md`, reply with:

- Where the final MP4 is (`projects/<name>/final.mp4`), and open the folder
- Length, format, and credits used
- One line: "Want any clip changed? Tell me which one and what."

If they ask for a change, redo only that clip (within the budget, with their OK on the cost), then assemble a new final video under a new filename.
