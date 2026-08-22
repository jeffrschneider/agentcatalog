---
name: try-a-candidate-model-against-live-leads
description: Runs a proposed model beside the one in force so both score real leads while only the current one routes, and reports what the change would do to the tiers and the territory queues. Use it when running `ref/mkt/lead-scoring-model`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Try a candidate model against live leads

## What it does

Runs a proposed model beside the one in force so both score real leads
while only the current one routes, and reports what the change would do
to the tiers and the territory queues.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check What Each Does to Routing**
  - `ref/mkt/lead-scoring-model`, activity 10 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)
- **Run It Beside the Live Model**
  - `ref/mkt/lead-scoring-model`, activity 12 -
    [Maintain Lead Scoring Model](../../../../processes/marketing/lead-scoring-model.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
