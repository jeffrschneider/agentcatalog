---
name: load-the-allocations
description: The agent records each function's or budget owner's number where spend is tracked, at a version, with each reforecast beside the budget it leaves as it was, and says when in the year that money becomes available. Use it when running `ref/fin/reforecast-the-year`, `ref/fin/set-the-annual-budget` and `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: budget-keeper
  agent-version: "1"
---

# Load the allocations

## What it does

The agent records each function's or budget owner's number where spend
is tracked, at a version, with each reforecast beside the budget it
leaves as it was, and says when in the year that money becomes
available.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Issue the Budget at a Version**
  - `ref/fin/set-the-annual-budget`, activity 16 -
    [Set the Annual Budget](../../../../processes/finance/set-the-annual-budget.md)
- **Issue the Reforecast at a Version**
  - `ref/fin/reforecast-the-year`, activity 14 -
    [Reforecast the Year](../../../../processes/finance/reforecast-the-year.md)
- **Load the Allocations**
  - `ref/mkt/set-marketing-budget`, activity 13 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Phase the Money across the Year**
  - `ref/mkt/set-marketing-budget`, activity 10 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

## What to record

It leaves the budget at a version for the year, with one line per
function carrying what was allocated, what was already committed against
it before the year began, what has been drawn, and what is left. Every
change to an allocation goes in as a new version naming who approved it,
on what date, and which line the money moved from and to, and the
version it replaces stays where it was. Every draw is recorded against
the allocation it came from and the run that made it. The uncommitted
remainder is restated whenever a draw or a change lands. Once the
reconciliation for a period closes, that period's figures are frozen, so
a question about it a year later gets the same answer it got on the day.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
