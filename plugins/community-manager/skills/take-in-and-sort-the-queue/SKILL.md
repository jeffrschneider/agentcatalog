---
name: take-in-and-sort-the-queue
description: Collects everything that arrived, which is the new posts, the questions and the reports, then types each item and puts it in order of urgency so the most pressing gets answered first. Use it when running `ref/mkt/moderate-community`.
license: CC-BY-4.0
metadata:
  agent: community-manager
  agent-version: "1"
---

# Take in and sort the queue

## What it does

Collects everything that arrived, which is the new posts, the questions
and the reports, then types each item and puts it in order of urgency so
the most pressing gets answered first.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Gather What Came In**
  - `ref/mkt/moderate-community`, activity 2 -
    [Moderate User Community](../../../../processes/marketing/moderate-community.md)
- **Sort the Queue**
  - `ref/mkt/moderate-community`, activity 3 -
    [Moderate User Community](../../../../processes/marketing/moderate-community.md)

## What to record

Every reply logged, every escalation with the reason it was flagged, and
a recurring-questions summary at the cadence the process sets.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
