---
name: cut-a-population-into-groups
description: Cuts a customer base or a market into groups that behave differently, describes each group and how buying works inside it, and checks that each group really does hold together and stand apart from the rest. Use it when running `ref/mkt/analyze-customer-base`, `ref/mkt/develop-marketing-strategy` and `ref/mkt/segment-the-market`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Cut a population into groups

## What it does

Cuts a customer base or a market into groups that behave differently,
describes each group and how buying works inside it, and checks that
each group really does hold together and stand apart from the rest.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Group the Base**
  - `ref/mkt/analyze-customer-base`, activity 8 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Map the Market and Its Segments**
  - `ref/mkt/develop-marketing-strategy`, activity 3 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
- **Test Whether the Segments Hold Apart**
  - `ref/mkt/segment-the-market`, activity 8 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)

## What to record

Every model at a version, saying which data it was fit on, over what
period, and which records it left out and why. Every prediction with the
model version that produced it and the inputs it was computed from, so
somebody can run it again and see whether the answer still holds. Every
assumption written beside the number it drives, naming where the
assumption came from and how far the number moves when the assumption
moves. A back-test result whenever the agent says a profile would have
picked the right customers, showing what the profile would have selected
and what actually happened to those accounts. A list of every rate it
could not source, marked unsourced, carried into the report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
