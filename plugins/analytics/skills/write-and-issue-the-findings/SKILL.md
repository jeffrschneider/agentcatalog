---
name: write-and-issue-the-findings
description: The agent writes each finding with the figures under it and issues the set at a numbered version that says what changed since the last one. Use it when running `ref/mkt/analyze-customer-base` and `ref/sup/report-what-customers-say`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Write and issue the findings

## What it does

The agent writes each finding with the figures under it and issues the
set at a numbered version that says what changed since the last one.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Issue the Findings as a Version**
  - `ref/mkt/analyze-customer-base`, activity 16 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Put the Evidence under Each Finding**
  - `ref/sup/report-what-customers-say`, activity 8 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)
- **Write the Findings**
  - `ref/mkt/analyze-customer-base`, activity 14 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
