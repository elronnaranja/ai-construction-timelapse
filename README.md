# AI Construction Timelapse — ChatGPT Makes the Whole Video

Make the viral "empty lot → finished dream house" timelapse video, with real construction sounds and no music.

Nothing to copy, no prompts to edit, no video editor. You answer a few questions and get the final video.

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

**2. Answer its questions.** Where it is, what the lot looks like now, the house you want, pool or no pool, vertical or horizontal, and your credit limit. No idea yet? Say "surprise me".

**3. Sign in to Google Flow** if Codex asks you to. It opens Flow in its browser; you sign in yourself.

**4. Say yes or no when it asks.** It only stops for:
- the finished house design, before it makes anything else
- the credit cost, before it spends anything
- anything Flow asks you to accept

**5. Get your video.** Codex makes the images, makes the clips in Flow, checks the sound and picture, joins everything and opens the folder with `final.mp4`.

Want a clip changed? Tell Codex which clip and what. It redoes only that one.

---

## Make another one

You only clone once. Next time, open the same folder in Codex and say:

```
Make me another construction video.
```

It asks the questions again and starts a new project. Your past videos stay in `projects/`.

Stopped halfway (out of credits, closed the app)? Open the same folder and say **"continue my construction video"**. It picks up where it left off without redoing finished clips.

---

## Good to know

- **Credits:** Codex shows the live Flow cost and waits for your OK. It never buys credits.
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
| `assemble.py` | Joins the clips and keeps the construction sound |
| `preferences.json` | Defaults: construction sounds on, no music |
| `CLAUDE.md`, `START-HERE.md` | Same workflow for Claude Code |
| `archive/assemble_silent.py` | Old silent version. Only if you want no sound |
