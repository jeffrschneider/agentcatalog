---
name: map-the-market-and-its-segments
description: The segments, their size, and how buyers buy in each. Use it when running `ref/mkt/develop-marketing-strategy`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Map the Market and Its Segments

## What happens

The segments, their size, and how buyers buy in each.

## Where it happens

- `ref/mkt/develop-marketing-strategy`, activity 3 -
  [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)

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
