---
name: record-what-the-round-rests-on
description: The assumptions, and what would reopen the ranking. Use it when running `ref/mkt/prioritize-initiatives`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Record What the Round Rests On

## What happens

The assumptions, and what would reopen the ranking.

## Where it happens

- `ref/mkt/prioritize-initiatives`, activity 16 -
  [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)

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
