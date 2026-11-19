---
name: check-the-sources-agree
description: When more than one system keeps its own count of the same thing, such as the headcount in the HR system, the pay in the payroll system and the labor cost in the ledger, the agent sets the counts side by side and names every difference and the system it starts in before any figure is reported. Use it when running `ref/hr/report-on-the-workforce`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Check the sources agree

## What it does

When more than one system keeps its own count of the same thing, such as
the headcount in the HR system, the pay in the payroll system and the
labor cost in the ledger, the agent sets the counts side by side and
names every difference and the system it starts in before any figure is
reported.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check the Sources Agree**
  - `ref/hr/report-on-the-workforce`, activity 7 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
