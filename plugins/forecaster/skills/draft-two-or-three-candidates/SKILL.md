---
name: draft-two-or-three-candidates
description: Writes two or three candidate answers to the question on the table, each one written down with the evidence and the assumptions under it. Use it when running `ref/mkt/attribution-model` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Draft two or three candidates

## What it does

Writes two or three candidate answers to the question on the table, each
one written down with the evidence and the assumptions under it.

## Where it happens

The agent does this in six activities across six reference processes.
Each one names the activity as that process words it.

- **Draft the Candidate Mixes**
  - `ref/mkt/media-plan`, activity 6 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Draft the Candidate Models**
  - `ref/mkt/attribution-model`, activity 7 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- **Draft the Candidate Profiles**
  - `ref/mkt/ideal-customer-profile`, activity 6 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Draft the Strategic Options**
  - `ref/mkt/develop-marketing-strategy`, activity 6 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
- **Draw the Candidate Divisions**
  - `ref/mkt/segment-the-market`, activity 7 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Fit the Candidate Models**
  - `ref/mkt/lead-scoring-model`, activity 8 -
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
