---
name: record-the-rules-and-the-assumptions
description: The agent writes down what the budget rests on, what would reopen it, and who may move money between functions and when. Use it when running `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: budget-keeper
  agent-version: "1"
---

# Record the rules and the assumptions

## What it does

The agent writes down what the budget rests on, what would reopen it,
and who may move money between functions and when.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Record What the Budget Rests On**
  - `ref/mkt/set-marketing-budget`, activity 15 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Set the Rules for Moving Money**
  - `ref/mkt/set-marketing-budget`, activity 9 -
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
