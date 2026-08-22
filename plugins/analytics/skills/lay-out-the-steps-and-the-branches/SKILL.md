---
name: lay-out-the-steps-and-the-branches
description: The agent sets out the order of the steps, the waits between them and the condition on every branch, and changes the ones the numbers argue against once the sequence has been running. Use it when running `ref/mkt/nurture-sequence`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Lay out the steps and the branches

## What it does

The agent sets out the order of the steps, the waits between them and
the condition on every branch, and changes the ones the numbers argue
against once the sequence has been running.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Map the Steps and the Branches**
  - `ref/mkt/nurture-sequence`, activity 4 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Tune the Branches**
  - `ref/mkt/nurture-sequence`, activity 16 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
