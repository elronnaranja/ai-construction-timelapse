# AI Construction Timelapse — ChatGPT Makes the Whole Video

Make the viral "empty lot → finished dream house" timelapse video, with a separate construction-sound layer and no music.

Nothing to copy, no prompts to edit, no video editor. Answer the initial questions for each new video; the agent then runs through routine steps automatically.

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

**2. Answer the initial questions.** The agent always starts each new video by asking about the setting, starting condition, finished house/storey count, pool or special features, unchanged surroundings and orientation. It summarizes details you already supplied and asks only what is missing; a complete brief gets one initial confirmation. Include any house, setting or background details you care about, or say "surprise me". Default: portrait 9:16, six images and five transitions.

Your answers apply to this video only. This initial exchange is the only planned typing; afterward, the agent handles routine work and asks only when a new requirement or blocker needs your decision.

**3. Connect the browser before generation.** Follow [BROWSER-SETUP.md](BROWSER-SETUP.md) for built-in Browser or Chrome integration setup. The agent must verify real Flow UI access and supported uploads/downloads before creating images or spending credits. A fresh install or full access alone does not establish browser control. Complete required setup/permission clicks and sign in to Flow yourself. Use an account with at least 50 available credits.

**4. Let the agent run.** Your request authorizes up to 50 existing credits: five transitions × 10 credits, one output each, no purchases. It checks the expected visible setting once and proceeds without repeated cost or design approvals. Prompts are prepared in advance and entered with a single fill/paste each. It stops only for a real blocker, required new legal consent.

**5. Get your video.** The agent creates images and clips, adds separate construction effects, checks picture and sound, and assembles `final.mp4`. The actual exported MP4 is embedded/attached in the final chat with a download link; an HTML preview is not the final delivery.

Optional: on a trusted checkout, allow file, browser and command access in your agent app to reduce permission prompts. Full access is optional; it does not replace Google login or required consent. Codex and Claude use their own permission settings.

Want a clip changed? Tell Codex which clip and what. It redoes only that one.

---

## Make another one

You only clone once. Next time, open the same folder in Codex and say:

```
Make me another construction video.
```

It asks the initial questions again and starts a new project. Your past videos stay in `projects/`.

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
| `assemble.py` | Joins Flow visuals with separate effects; never uses Flow audio |
| `preferences.json` | Defaults: construction sounds on, no music |
| `CLAUDE.md`, `START-HERE.md` | Same workflow for Claude Code |
| `archive/assemble_silent.py` | Old silent version. Only if you want no sound |

## Audio assembly is automatic

Flow audio is never used in the export. The agent sources five separate scene-matched, appropriately licensed construction-effect tracks and automatically combines them with the visuals. There is no listening-review approval step or review JSON requirement. Audio stream, decode and source-file separation checks still run. Record effect sources/rights in the manifest; do not reuse extracted Flow audio. These checks do not detect music inside a mislabeled third-party effect.

All Flow SOUND instructions remain ALL CAPS. Final delivery includes the actual exported MP4 in chat. The final design locks the storey count and roof height throughout all clips.
