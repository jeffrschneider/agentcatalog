---
name: turn-a-signed-plan-into-tracked-items
description: Takes the milestones a signed plan carries and makes each one an item with one owner, one date and a state, traceable to the line of the plan it came from. Use it when running `ref/prt/write-a-joint-plan`.
license: CC-BY-4.0
metadata:
  agent: commitment-keeper
  agent-version: "1"
---

# Turn a signed plan into tracked items

## What it does

Takes the milestones a signed plan carries and makes each one an item
with one owner, one date and a state, traceable to the line of the plan
it came from.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Record the Commitments**
  - `ref/prt/write-a-joint-plan`, activity 15 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)
- **Set the Milestones and the Dates**
  - `ref/prt/write-a-joint-plan`, activity 10 -
    [Write a Joint Plan](../../../../processes/partners/write-a-joint-plan.md)

## What to record

Each commitment as an item carrying one owner, one date and a state,
traceable to the line of the signed plan it came from. At every review,
the roll-call of all of them with the late ones counted. Each closed
commitment with the reason it was given up on and the date. The
decisions from the review with the new owners and the new dates, and
every move of a date with the review that moved it, so a commitment that
has slipped twice can be seen to have slipped twice. The review dates
set for the year, and whose calendars they landed on.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
