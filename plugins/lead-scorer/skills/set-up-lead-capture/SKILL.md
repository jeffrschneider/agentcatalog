---
name: set-up-lead-capture
description: The scan, the fields, and the path into the CRM. Use it when running `ref/mkt/trade-show`.
license: CC-BY-4.0
metadata:
  agent: lead-scorer
  agent-version: "1"
---

# Set up Lead Capture

## What happens

The scan, the fields, and the path into the CRM.

## Where it happens

- `ref/mkt/trade-show`, activity 9 -
  [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)

## What to record

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
