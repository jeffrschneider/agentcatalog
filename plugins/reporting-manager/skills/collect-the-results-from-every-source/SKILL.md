---
name: collect-the-results-from-every-source
description: Asks every channel and every run for the same things, in the same format, by the same date, and pulls together what comes back with a source on every line. Use it when running `ref/mkt/brief-executive-leadership` and `ref/mkt/marketing-performance-report`.
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Collect the results from every source

## What it does

Asks every channel and every run for the same things, in the same
format, by the same date, and pulls together what comes back with a
source on every line.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Ask Every Source the Same Things**
  - `ref/mkt/marketing-performance-report`, activity 2 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Pull the Results for the Period**
  - `ref/mkt/brief-executive-leadership`, activity 4 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
