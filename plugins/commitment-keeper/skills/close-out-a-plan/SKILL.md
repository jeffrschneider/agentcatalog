---
name: close-out-a-plan
description: "At the end of a plan, records the last state of every item: met, carried into the next plan with its owner and its date, or closed with the reason. Use it when running `ref/hr/run-a-new-hires-first-months`."
license: CC-BY-4.0
metadata:
  agent: commitment-keeper
  agent-version: "1"
---

# Close out a plan

## What it does

At the end of a plan, records the last state of every item: met, carried
into the next plan with its owner and its date, or closed with the
reason. The plan closes with nothing left open by silence.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Close the Plan**
  - `ref/hr/run-a-new-hires-first-months`, activity 16 -
    [Run a New Hire's First Months](../../../../processes/human-resources/run-a-new-hires-first-months.md)

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
