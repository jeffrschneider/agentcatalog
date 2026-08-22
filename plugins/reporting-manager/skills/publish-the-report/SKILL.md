---
name: publish-the-report
description: Puts the report out on its date at a version, whether or not every source answered, with every line attributed to where it came from and the evidence under it. Use it when running `ref/mkt/brand-health`, `ref/mkt/marketing-performance-report` and `ref/mkt/reconcile-media-spend`.
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Publish the report

## What it does

Puts the report out on its date at a version, whether or not every
source answered, with every line attributed to where it came from and
the evidence under it.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Publish the Report**
  - `ref/mkt/marketing-performance-report`, activity 13 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Release the Figures**
  - `ref/mkt/reconcile-media-spend`, activity 13 -
    [Reconcile Media Spend](../../../../processes/marketing/reconcile-media-spend.md)
- **Report Awareness, Perception and Preference**
  - `ref/mkt/brand-health`, activity 22 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
