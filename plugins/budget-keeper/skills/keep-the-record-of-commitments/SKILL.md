---
name: keep-the-record-of-commitments
description: The agent records every contract, licence and renewal with its owner, cost, term and renewal date, and totals up what is already committed against a period before any new money is divided. Use it when running `ref/mkt/prioritize-initiatives`, `ref/mkt/select-marketing-technology` and `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: budget-keeper
  agent-version: "1"
---

# Keep the record of commitments

## What it does

The agent records every contract, licence and renewal with its owner,
cost, term and renewal date, and totals up what is already committed
against a period before any new money is divided.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **List the Money Already Committed**
  - `ref/mkt/set-marketing-budget`, activity 3 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Read What Is Already Committed**
  - `ref/mkt/prioritize-initiatives`, activity 4 -
    [Prioritize Marketing Initiatives](../../../../processes/marketing/prioritize-initiatives.md)
- **Write It into the Register**
  - `ref/mkt/select-marketing-technology`, activity 19 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)

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
