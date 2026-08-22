---
name: find-the-traits-that-separate-groups
description: Works out which traits separate one group from another, or separate the wins from everything else, and says which of those traits the division should be made on. Use it when running `ref/mkt/analyze-customer-base`, `ref/mkt/ideal-customer-profile` and `ref/mkt/segment-the-market`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Find the traits that separate groups

## What it does

Works out which traits separate one group from another, or separate the
wins from everything else, and says which of those traits the division
should be made on.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Choose the Dividing Traits**
  - `ref/mkt/segment-the-market`, activity 6 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Find What the Groups Share**
  - `ref/mkt/analyze-customer-base`, activity 10 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Find the Traits that Predict a Win**
  - `ref/mkt/ideal-customer-profile`, activity 5 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)

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
