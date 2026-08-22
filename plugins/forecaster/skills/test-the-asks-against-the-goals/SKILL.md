---
name: test-the-asks-against-the-goals
description: Whether the money asked for can reach the year's goals. Use it when running `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Test the Asks against the Goals

## What happens

Whether the money asked for can reach the year's goals.

## Where it happens

- `ref/mkt/set-marketing-budget`, activity 6 -
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
