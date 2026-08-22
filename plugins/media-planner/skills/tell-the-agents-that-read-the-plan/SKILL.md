---
name: tell-the-agents-that-read-the-plan
description: Every agent on the old split hears the new one. Use it when running `ref/mkt/reallocate-media-spend`.
license: CC-BY-4.0
metadata:
  agent: media-planner
  agent-version: "1"
---

# Tell the Agents that Read the Plan

## What happens

Every agent on the old split hears the new one.

## Where it happens

- `ref/mkt/reallocate-media-spend`, activity 13 -
  [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)

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
