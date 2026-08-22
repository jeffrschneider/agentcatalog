---
name: settle-a-lead-no-rule-can-place
description: Holds a lead that no routing rule settles, puts it to a person with everything known about it, and applies the answer that comes back. Use it when running `ref/mkt/lead-routing`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Settle a lead no rule can place

## What it does

Holds a lead that no routing rule settles, puts it to a person with
everything known about it, and applies the answer that comes back.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Clear the Exception**
  - `ref/mkt/lead-routing`, activity 6 -
    [Route Inbound Lead](../../../../processes/marketing/lead-routing.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
