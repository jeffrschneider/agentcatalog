---
name: score-a-partner-against-its-plan
description: Scores each partner against the plan it agreed to, writes the finding as on plan, behind or at risk, and refers any result that would move a tier into the tiering round, where the published rules decide it. Use it when running `ref/prt/review-partner-performance`.
license: CC-BY-4.0
metadata:
  agent: tier-assessor
  agent-version: "1"
---

# Score a partner against its plan

## What it does

Scores each partner against the plan it agreed to, writes the finding as
on plan, behind or at risk, and refers any result that would move a tier
into the tiering round, where the published rules decide it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Draft the Finding per Partner**
  - `ref/prt/review-partner-performance`, activity 9 -
    [Review Partner Performance](../../../../processes/partners/review-partner-performance.md)
- **Refer the Tier Changes**
  - `ref/prt/review-partner-performance`, activity 14 -
    [Review Partner Performance](../../../../processes/partners/review-partner-performance.md)
- **Score Each Partner Against the Plan**
  - `ref/prt/review-partner-performance`, activity 7 -
    [Review Partner Performance](../../../../processes/partners/review-partner-performance.md)

## What to record

The rules at the version in force, and the date they were published. The
evidence per partner, each line naming the system and the date it was
read from, with every gap marked as a gap. The tier the rules gave, with
the inputs it was computed from, so somebody else can recompute it from
what was written down. Every exception with its reason, the person
asking, the signer, and the date it expires, counted in the published
round. In a performance round, the score with the rules version beside
it, the finding said as on plan, behind or at risk, and the referral
with the score and the date behind it. At an exit, the access that was
taken down and when. At the close, where the rules gave a tier nobody
could defend, and what the next version should say.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
