---
name: find-the-groups-in-the-base
description: The agent cuts a base into groups that behave differently and says which traits separate one outcome from another, with the evidence for why each group is a group. Use it when running `ref/mkt/analyze-customer-base` and `ref/mkt/ideal-customer-profile`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Find the groups in the base

## What it does

The agent cuts a base into groups that behave differently and says which
traits separate one outcome from another, with the evidence for why each
group is a group.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Find the Traits that Predict a Win**
  - `ref/mkt/ideal-customer-profile`, activity 5 -
    [Define Ideal Customer Profile](../../../../processes/marketing/ideal-customer-profile.md)
- **Group the Base**
  - `ref/mkt/analyze-customer-base`, activity 8 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
