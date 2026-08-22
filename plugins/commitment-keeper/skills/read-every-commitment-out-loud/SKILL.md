---
name: read-every-commitment-out-loud
description: Reads every commitment at review with its owner, its date and its state, marked met, running, late or untouched, so nothing stays open by silence. Use it when running `ref/prt/review-a-joint-plan`.
license: CC-BY-4.0
metadata:
  agent: commitment-keeper
  agent-version: "1"
---

# Read every commitment out loud

## What it does

Reads every commitment at review with its owner, its date and its state,
marked met, running, late or untouched, so nothing stays open by
silence.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Read the Commitments**
  - `ref/prt/review-a-joint-plan`, activity 5 -
    [Review a Joint Plan](../../../../processes/partners/review-a-joint-plan.md)

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
