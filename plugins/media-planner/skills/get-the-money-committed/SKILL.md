---
name: get-the-money-committed
description: Puts a split and an amount in front of the people who own the money, and records what they committed and when. Use it when running `ref/mkt/media-plan` and `ref/mkt/test-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: media-planner
  agent-version: "1"
---

# Get the money committed

## What it does

Puts a split and an amount in front of the people who own the money, and
records what they committed and when.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Choose the Mix**
  - `ref/mkt/media-plan`, activity 8 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Commit the Test Budget**
  - `ref/mkt/test-ad-creative`, activity 6 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Get the Plan Approved**
  - `ref/mkt/media-plan`, activity 12 -
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
