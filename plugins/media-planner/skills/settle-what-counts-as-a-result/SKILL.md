---
name: settle-what-counts-as-a-result
description: Says what the plan is judged on and where that result is counted, so every channel is read the same way afterwards. Use it when running `ref/mkt/media-plan`.
license: CC-BY-4.0
metadata:
  agent: media-planner
  agent-version: "1"
---

# Settle what counts as a result

## What it does

Says what the plan is judged on and where that result is counted, so
every channel is read the same way afterwards.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Settle What Counts as a Result**
  - `ref/mkt/media-plan`, activity 11 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)

## What to record

The plan at a numbered version, one row per line: the channel, the dates
it runs, the weight it runs at, the audience it is bought against, and
the money committed to it. Every earlier version stays readable at its
own number, so a buy can be checked against the plan it was placed
under. A change record for each version, saying which lines moved, by
how much, why, and who approved it. A dated position saying what is
committed, what has been placed, and what is still free, with the
figures those came from. Every request for money the plan could not
cover, with the amount asked for and the answer it got.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
