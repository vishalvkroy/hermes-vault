# Video concept (secondary channel, concept saved — generation not submitted)

**Format:** 20-25s vertical, talking-head style (HeyGen avatar path) or screen-capture-style dev
diary (Kling), matching the postmortem/build-in-public angle of the Reddit and LinkedIn posts
rather than a polished feature ad.

**Brief:** Same story as the Reddit/LinkedIn posts — the silently-dead curiosity ranker
(`vector.length === 21` vs an actual 29-category vector) — told as a quick, honest dev-diary
clip.

## Scene breakdown

1. (0-4s) Hook, direct to camera: "Our recommendation feed was broken for months. Nothing ever
   crashed."
2. (4-10s) Screen capture: the offending line, `curiosityVector.length === 21`, next to the
   category list scrolled to show 29 entries.
3. (10-16s) Direct to camera: quick explain — the category list grew, the check didn't, so
   personalization silently fell back to "just show popular stuff" for however long that gap
   existed.
4. (16-21s) Screen capture: the fix — checking against the real list length, plus the
   self-healing rebuild trigger.
5. (21-25s) Direct to camera close: "No alert ever fired for this. What's the quietest bug you've
   shipped?"

**Status:** concept saved via `video_create_concept` — concept id
`014ab6c6-aa76-4c14-ac62-8f9636f9ccd8`. No generation job submitted.

**Provider note:** Not submitted for generation. `video_heygen_usage()` checked — 0/3 used this
month, 3 remaining, headroom whenever Vishal approves the HeyGen path. Kling (fal.ai) still needs
Vishal's credit setup; `video_generate(provider="kling")` is expected to 503 "not configured"
until that's done — not a bug if/when tried. Per the skill, submitting either generation job is
an approval-gated, cost-bearing action, not something done automatically while drafting.
