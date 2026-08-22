---
name: build-one-clean-record-from-a-submission
description: Takes an incoming submission, merges it into any record already held for the same person or company, and fills in the company size, industry and geography that the model needs and the form did not ask for. Use it when running `ref/mkt/lead-routing`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Build one clean record from a submission

## What it does

Takes an incoming submission, merges it into any record already held for
the same person or company, and fills in the company size, industry and
geography that the model needs and the form did not ask for.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Capture and Dedupe**
  - `ref/mkt/lead-routing`, activity 1 -
    [Route Inbound Lead](../../../../processes/marketing/lead-routing.md)
- **Enrich**
  - `ref/mkt/lead-routing`, activity 2 -
    [Route Inbound Lead](../../../../processes/marketing/lead-routing.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
