---
name: set-the-scope-of-the-report
description: "Writes down what the report covers before anything is gathered: the period, the runs inside it, the channels and conversions in scope, and the questions the report has to answer. Use it when running `ref/mkt/attribution-model` and `ref/mkt/marketing-performance-report`."
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Set the scope of the report

## What it does

Writes down what the report covers before anything is gathered: the
period, the runs inside it, the channels and conversions in scope, and
the questions the report has to answer.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Set What the Report Covers**
  - `ref/mkt/marketing-performance-report`, activity 1 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Set What the Review Covers**
  - `ref/mkt/attribution-model`, activity 3 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
