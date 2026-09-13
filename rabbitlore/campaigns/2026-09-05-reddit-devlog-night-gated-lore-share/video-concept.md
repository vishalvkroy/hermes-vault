# Video concept (secondary channel, concept saved — generation not submitted)

**Status:** concept saved via `video_create_concept` — concept id
`cecc601e-abe7-41bf-8f37-b07756b50d51`. No generation job submitted (HeyGen or Kling) — that step
needs Vishal's explicit go-ahead per the skill, since it spends a scarce free-tier slot (HeyGen,
3/month) or real fal.ai credit (Kling). Checked `video_heygen_usage()`: 0/3 used this month, 3
remaining — HeyGen path has headroom whenever Vishal approves. Kling path (fal.ai) still needs
Vishal's credit setup; expect a 503 "not configured" if `video_generate(provider="kling")` is
tried before that.

**Format:** 20-25s vertical, talking-head style (HeyGen avatar path) or UGC-style product clip
(Kling), matching the Reddit post's build-in-public angle rather than a polished ad.

**Brief:** Same story as the Reddit post — the 11pm-4am lore-share gate — told in first person as a
quick dev-diary clip, not a feature-tour ad.

## Scene breakdown

1. (0-4s) Hook, direct to camera: "We locked a feature so it only works between 11pm and 4am."
2. (4-10s) Screen capture: the lore-share card appearing in a DM/room, timestamp visible showing
   late-night hours.
3. (10-16s) Direct to camera: quick explain, most raw stories already get posted late at night, so
   the gate pushes sharing toward the heavier stuff instead of daytime safe posts.
4. (16-21s) Screen capture: locked-state screen shown during the day, for the honest "here's the
   tradeoff" beat.
5. (21-25s) Direct to camera close: "Still deciding if we add a tooltip or leave the friction in.
   What would you do?"

**Provider note:** if HeyGen (avatar talking-head) is used, need Vishal to confirm remaining
monthly free-tier quota first. If Kling (screen-capture-style product clip) is used, generation
will 503 until Vishal's fal.ai credit is set up — expected, not a failure, per the skill.
