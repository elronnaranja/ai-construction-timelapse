# AI Construction Timelapse — ChatGPT Makes the Whole Video

Make the viral "empty lot → finished dream house" timelapse video, with a separate reviewed construction-sound layer and no music.

Nothing to copy, no prompts to edit, no video editor. Describe your idea; the agent uses saved defaults and runs through routine steps automatically.

---

## What you need

- **ChatGPT Plus** (it includes **Codex**)
- The **ChatGPT app** on a computer (Mac or Windows), signed in, with **Codex** and its **browser access** on
- A **Google account** with **Flow credits** (about 50 credits for one video)

> Use a computer, not a phone. Codex has to open Google Flow and save the video files.

---

## How to make a video

**1. Open ChatGPT on your computer, go to Codex and send it this:**

```
Clone https://github.com/elronnaranja/ai-construction-timelapse and make me a construction video.
```

**2. Describe your idea.** Include any house, setting or background details you care about, or say "surprise me". Default: portrait 9:16, six images and five transitions.

**3. Sign in to Google Flow** if needed. Use an account with at least 50 available credits.

**4. Let the agent run.** Your request authorizes up to 50 existing credits: five transitions × 10 credits, one output each, no purchases. It checks the expected visible setting once and proceeds without repeated cost or design approvals. Prompts are prepared in advance and entered with a single fill/paste each. It stops only for a real blocker, required new legal consent, or unavailable audio listening review.

**5. Get your video.** The agent creates images and clips, adds separately reviewed construction effects, checks picture and sound, and assembles `final.mp4`. The actual exported MP4 is embedded/attached in the final chat with a download link; an HTML preview is not the final delivery.

Optional: on a trusted checkout, allow file, browser and command access in your agent app to reduce permission prompts. Full access is optional; it does not replace Google login or required consent. Codex and Claude use their own permission settings.

Want a clip changed? Tell Codex which clip and what. It redoes only that one.

---

## Make another one

You only clone once. Next time, open the same folder in Codex and say:

```
Make me another construction video.
```

It reuses your defaults and starts a new project. Your past videos stay in `projects/`.

Stopped halfway (out of credits, closed the app)? Open the same folder and say **"continue my construction video"**. It picks up where it left off without redoing finished clips.

---

## Good to know

- **Credits:** The standard preset uses 50 Flow credits, not chat tokens. If your account has 50 free credits available, this Flow render has no additional cash cost. Free allocations, eligibility and pricing can change; this is not a promise of 50 free credits daily. Image generation and agent usage depend on your existing plan. The agent never buys credits.
- **Out of credits?** It stops and saves everything. Say "continue" later.
- **Your login stays yours:** you sign in to Google yourself. Never paste a password into the chat.
- **It's AI:** some steps may morph a little between stages. It's a creative timelapse, not an engineering plan.
- **Your files stay on your computer:** videos and images go in `projects/` and are never uploaded to GitHub.

---

## What's in this repo

| File | What it is |
|---|---|
| `AGENTS.md` | Tells Codex what to ask you and how to run everything |
| `WORKFLOW.md` | The full step-by-step production instructions |
| `assemble.py` | Joins Flow visuals with separate reviewed effects; never uses Flow audio |
| `audio-review.example.json` | Required listening review with clip/SFX hashes and usage rights |
| `preferences.json` | Defaults: construction sounds on, no music |
| `CLAUDE.md`, `START-HERE.md` | Same workflow for Claude Code |
| `archive/assemble_silent.py` | Old silent version. Only if you want no sound |

## Why Flow music cannot leak into assembly

Flow can ignore “no music” prompts. This workflow therefore never uses its audio. Five separately sourced construction/scene-effect tracks must pass a listening review before the assembler will run. Missing approval or changed files block delivery. There is no “keep raw audio” fallback and no automatic mute-everything shortcut.

This requires clean effects and an actual listener. An audio stream or speech detector cannot prove music is absent. If listening isn't available to the agent, a reviewer must approve the tracks and final mix before delivery. Music-free output cannot be certified by prompts alone.

All Flow SOUND instructions use ALL CAPS and explicitly exclude TV static, buzzing and distorted audio in addition to music. Prompt wording remains advisory; the separate reviewed sound layer remains required.

The final design locks the storey count and roof height for every stage. A two-storey house must never grow a temporary third floor and remove it later. Intermediate frames are checked throughout each clip; architecture violations fail visual review even when the final frame looks correct.
