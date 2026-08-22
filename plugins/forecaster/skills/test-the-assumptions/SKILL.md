---
name: test-the-assumptions
description: Moves each assumption one at a time and records how far the answer swings, so it is clear which assumptions the number actually depends on. Use it when running `ref/mkt/size-market-opportunity`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Test the assumptions

## What it does

Moves each assumption one at a time and records how far the answer
swings, so it is clear which assumptions the number actually depends on.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Test the Assumptions**
  - `ref/mkt/size-market-opportunity`, activity 9 -
    [Size Market Opportunity](../../../../processes/marketing/size-market-opportunity.md)

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
