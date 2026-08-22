---
name: put-the-reviews-on-the-calendar
description: Sets how often the plan is reviewed, opens each review on that cadence against the calendar of everyone the plan names, and dates the next one before the current one closes. Use it when running `ref/prt/review-a-joint-plan` and `ref/prt/write-a-joint-plan`.
license: CC-BY-4.0
metadata:
  agent: commitment-keeper
  agent-version: "1"
---

# Put the reviews on the calendar

## What it does

Sets how often the plan is reviewed, opens each review on that cadence
against the calendar of everyone the plan names, and dates the next one
before the current one closes.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Open the Review**
  - `ref/prt/review-a-joint-plan`, activity 1 -
    [Review a Joint Plan](../../../../processes/partners/review-a-joint-plan.md)
- **Set the Next Review**
  - `ref/prt/review-a-joint-plan`, activity 17 -
    [Review a Joint Plan](../../../../processes/partners/review-a-joint-plan.md)
- **Set the Review Cadence**
  - `ref/prt/write-a-joint-plan`, activity 17 -
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
