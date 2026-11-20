---
name: tell-the-agents-what-was-decided
description: Once a decision is made, the agent tells every agent and budget owner that has to act what was decided about the money, what each one now holds and what moved since the last version. Use it when running `ref/fin/reforecast-the-year`, `ref/fin/set-the-annual-budget` and `ref/mkt/brief-executive-leadership`.
license: CC-BY-4.0
metadata:
  agent: budget-keeper
  agent-version: "1"
---

# Tell the agents what was decided

## What it does

Once a decision is made, the agent tells every agent and budget owner
that has to act what was decided about the money, what each one now
holds and what moved since the last version.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Hand the Decisions On**
  - `ref/mkt/brief-executive-leadership`, activity 19 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)
- **Tell Each Budget Owner What They Hold**
  - `ref/fin/set-the-annual-budget`, activity 17 -
    [Set the Annual Budget](../../../../processes/finance/set-the-annual-budget.md)
- **Tell the Budget Owners What Changed**
  - `ref/fin/reforecast-the-year`, activity 15 -
    [Reforecast the Year](../../../../processes/finance/reforecast-the-year.md)

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
