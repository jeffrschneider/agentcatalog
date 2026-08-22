---
name: set-the-flighting-and-the-weights
description: "Writes the running detail for each line of the plan: the dates it runs, the money it gets in each period, where it runs, and how much weight it carries against the other lines. Use it when running `ref/mkt/account-based-play` and 3 other reference processes."
license: CC-BY-4.0
metadata:
  agent: media-planner
  agent-version: "1"
---

# Set the flighting and the weights

## What it does

Writes the running detail for each line of the plan: the dates it runs,
the money it gets in each period, where it runs, and how much weight it
carries against the other lines.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Lay out the Flighting**
  - `ref/mkt/media-plan`, activity 9 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Set the Flights, Budgets and Rotation**
  - `ref/mkt/traffic-ad-creative`, activity 13 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Set the Parameters**
  - `ref/mkt/display-retargeting`, activity 2 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Set the Tiers and the Weight**
  - `ref/mkt/account-based-play`, activity 3 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)

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
