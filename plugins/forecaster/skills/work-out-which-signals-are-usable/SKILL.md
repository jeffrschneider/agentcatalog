---
name: work-out-which-signals-are-usable
description: Assembles the facts that might predict a fit or a win, records where each one comes from, and measures how often each is actually filled in and what it costs to get. Use it when running `ref/mkt/ideal-customer-profile` and `ref/mkt/lead-scoring-model`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Work out which signals are usable

## What it does

Assembles the facts that might predict a fit or a win, records where
each one comes from, and measures how often each is actually filled in
and what it costs to get.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Gather the Candidate Signals**
  - `ref/mkt/lead-scoring-model`, activity 5 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Name the Qualifying Signals**
  - `ref/mkt/ideal-customer-profile`, activity 7 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Test the Signal Coverage**
  - `ref/mkt/ideal-customer-profile`, activity 8 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
  - `ref/mkt/lead-scoring-model`, activity 7 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)

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
