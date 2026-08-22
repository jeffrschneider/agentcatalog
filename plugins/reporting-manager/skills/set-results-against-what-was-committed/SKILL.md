---
name: set-results-against-what-was-committed
description: Puts each result next to what that run said it would do and next to what the plan said the year would produce, so the difference sits on the same line. Use it when running `ref/mkt/marketing-performance-report`, `ref/mkt/quarterly-business-review` and `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: reporting-manager
  agent-version: "1"
---

# Set results against what was committed

## What it does

Puts each result next to what that run said it would do and next to what
the plan said the year would produce, so the difference sits on the same
line. It does the same for money being asked for, saying whether the
amount could reach the goals it is meant to.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Set Results Beside What Was Expected**
  - `ref/mkt/marketing-performance-report`, activity 9 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Set the Quarter against the Annual Goals**
  - `ref/mkt/quarterly-business-review`, activity 3 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Test the Asks against the Goals**
  - `ref/mkt/set-marketing-budget`, activity 6 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

## What to record

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
