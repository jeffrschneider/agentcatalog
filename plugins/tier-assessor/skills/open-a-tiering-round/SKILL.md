---
name: open-a-tiering-round
description: Starts a round, reads the tiering rules at the version in force with the date they were published, and checks that the same evidence is present for every partner in scope. Use it when running `ref/prt/set-a-partner-tier`.
license: CC-BY-4.0
metadata:
  agent: tier-assessor
  agent-version: "1"
---

# Open a tiering round

## What it does

Starts a round, reads the tiering rules at the version in force with the
date they were published, and checks that the same evidence is present
for every partner in scope. A gap is marked as a gap rather than counted
as a zero.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check the Evidence Is Complete**
  - `ref/prt/set-a-partner-tier`, activity 4 -
    [Set a Partner Tier](../../../../processes/partners/set-a-partner-tier.md)
- **Open the Tiering Round**
  - `ref/prt/set-a-partner-tier`, activity 1 -
    [Set a Partner Tier](../../../../processes/partners/set-a-partner-tier.md)
- **Read the Rules in Force**
  - `ref/prt/set-a-partner-tier`, activity 2 -
    [Set a Partner Tier](../../../../processes/partners/set-a-partner-tier.md)

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
