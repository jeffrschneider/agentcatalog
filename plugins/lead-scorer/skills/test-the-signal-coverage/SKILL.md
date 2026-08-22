---
name: test-the-signal-coverage
description: How often each signal is filled in, and what it costs. Use it when running `ref/mkt/ideal-customer-profile` and `ref/mkt/lead-scoring-model`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Test the Signal Coverage

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/ideal-customer-profile`, how often each signal is filled
  in, and what it costs
- in `ref/mkt/lead-scoring-model`, how often each signal is filled in,
  and how early

## Where it happens

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
