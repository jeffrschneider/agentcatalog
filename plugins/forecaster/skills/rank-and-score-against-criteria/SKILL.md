---
name: rank-and-score-against-criteria
description: Scores each candidate against criteria that were fixed beforehand and puts them in order, naming the criterion behind every verdict and the evidence each place rests on. Use it when running `ref/mkt/engage-marketing-agency` and `ref/mkt/segment-the-market`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Rank and score against criteria

## What it does

Scores each candidate against criteria that were fixed beforehand and
puts them in order, naming the criterion behind every verdict and the
evidence each place rests on.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Rank the Segments**
  - `ref/mkt/segment-the-market`, activity 13 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Score the Proposals**
  - `ref/mkt/engage-marketing-agency`, activity 10 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)

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
