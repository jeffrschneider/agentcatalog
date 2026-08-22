---
name: pick-the-accounts-and-the-plays
description: Picks the accounts and segments both sides go after together, with the reason written on each one and the conflict or the owner behind every account removed, then names the plays run against them. Use it when running `ref/prt/write-a-joint-plan`.
license: CC-BY-4.0
metadata:
  agent: joint-planner
  agent-version: "1"
---

# Pick the accounts and the plays

## What it does

Picks the accounts and segments both sides go after together, with the
reason written on each one and the conflict or the owner behind every
account removed, then names the plays run against them.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Name the Plays**
  - `ref/prt/write-a-joint-plan`, activity 9 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)
- **Pick the Accounts and Segments**
  - `ref/prt/write-a-joint-plan`, activity 5 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)

## What to record

The targets at a version, with the person on each side who confirmed
them. The account list with the reason written on each one, and every
account removed with the conflict or the owner behind it. The inputs per
side with a name against each line, and what our side costs against the
budget line it comes from. The milestones with one owner and one date
each. The plan at a version, with every blank filled or marked open. At
review, the gaps with the reason and the person closest to each, the
decision as both sponsors announced it, and the amendment with the
changed lines marked against the version they replace. Anybody auditing
a run can read what each side promised, what it cost, and what changed
since.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
