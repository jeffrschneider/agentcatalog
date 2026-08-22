---
name: test-whether-the-data-supports-a-definition
description: "Checks whether the data on hand can carry a proposed model or a proposed set of segments: how often each signal is filled in, what it costs to fill, and whether the people described can be found and reached at all. Use it when running `ref/mkt/ideal-customer-profile`, `ref/mkt/lead-scoring-model` and `ref/mkt/segment-the-market`."
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Test whether the data supports a definition

## What it does

Checks whether the data on hand can carry a proposed model or a proposed
set of segments: how often each signal is filled in, what it costs to
fill, and whether the people described can be found and reached at all.

## Where it happens

The agent does this in two activities across three reference processes.
Each one names the activity as that process words it.

- **Test Whether Each Segment Can Be Reached**
  - `ref/mkt/segment-the-market`, activity 10 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Test the Signal Coverage**
  - `ref/mkt/ideal-customer-profile`, activity 8 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
  - `ref/mkt/lead-scoring-model`, activity 7 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
