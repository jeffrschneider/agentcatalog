---
name: say-what-data-is-on-hand
description: The agent checks whether the systems already hold what the question needs, which fields exist and how complete each one is, and whether an earlier read already answers it. Use it when running `ref/mkt/customer-research` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Say what data is on hand

## What it does

The agent checks whether the systems already hold what the question
needs, which fields exist and how complete each one is, and whether an
earlier read already answers it. It says what is missing before the work
starts rather than partway through.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check What Is Already Known**
  - `ref/mkt/customer-research`, activity 2 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Check the Data on Hand**
  - `ref/mkt/target-audience-segment`, activity 3 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
