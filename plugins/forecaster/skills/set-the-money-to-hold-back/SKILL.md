---
name: set-the-money-to-hold-back
description: Says how much money to set aside and for how long, whether that is what an engagement may cost over its term or what is held back for changes during the year. Use it when running `ref/mkt/engage-marketing-agency` and `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Set the money to hold back

## What it does

Says how much money to set aside and for how long, whether that is what
an engagement may cost over its term or what is held back for changes
during the year.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Set the Budget and the Term**
  - `ref/mkt/engage-marketing-agency`, activity 5 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)
- **Size the Reserve**
  - `ref/mkt/set-marketing-budget`, activity 7 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

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
