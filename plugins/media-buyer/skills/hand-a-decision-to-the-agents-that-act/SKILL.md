---
name: hand-a-decision-to-the-agents-that-act
description: Passes a settled decision to each agent that has to act on it, including the money it has been given and the rules that come with it, and takes back what each one says it will change. Use it when running `ref/mkt/develop-marketing-strategy` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: media-buyer
  agent-version: "1"
---

# Hand a decision to the agents that act

## What it does

Passes a settled decision to each agent that has to act on it, including
the money it has been given and the rules that come with it, and takes
back what each one says it will change.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Hand over the Commitments**
  - `ref/mkt/prioritize-initiatives`, activity 15 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Hand over the Profile**
  - `ref/mkt/ideal-customer-profile`, activity 15 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Hand over the Segments**
  - `ref/mkt/segment-the-market`, activity 16 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Hand the Strategy to the Work that Follows**
  - `ref/mkt/develop-marketing-strategy`, activity 15 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
- **Tell Every Function What It Has**
  - `ref/mkt/set-marketing-budget`, activity 14 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

## What to record

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
