---
name: read-a-closed-period
description: Reads what a finished period actually produced, which covers what published and what slipped, how each thing did, what each function spent against what it was given, and what the last report could not answer. Use it when running `ref/mkt/annual-marketing-plan` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Read a closed period

## What it does

Reads what a finished period actually produced, which covers what
published and what slipped, how each thing did, what each function spent
against what it was given, and what the last report could not answer.

## Where it happens

The agent does this in four activities across five reference processes.
Each one names the activity as that process words it.

- **Read Last Year's Spend**
  - `ref/mkt/set-marketing-budget`, activity 2 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Read the Closed Period**
  - `ref/mkt/content-calendar`, activity 2 -
    [Plan Content Calendar](../../../../processes/marketing/content-calendar.md)
- **Read the Closed Periods**
  - `ref/mkt/annual-marketing-plan`, activity 2 -
    [Build Annual Marketing Plan](../../../../processes/marketing/annual-marketing-plan.md)
  - `ref/mkt/develop-marketing-strategy`, activity 2 -
    [Develop Marketing Strategy](../../../../processes/marketing/develop-marketing-strategy.md)
- **Take in the Period Report**
  - `ref/mkt/quarterly-business-review`, activity 2 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
