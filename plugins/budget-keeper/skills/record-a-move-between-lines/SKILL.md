---
name: record-a-move-between-lines
description: Once a person has approved it, the agent records money moving from one line of the plan to another as a new version, naming who approved it and which lines it came from and went to. Use it when running `ref/mkt/quarterly-business-review`.
license: CC-BY-4.0
metadata:
  agent: budget-keeper
  agent-version: "1"
---

# Record a move between lines

## What it does

Once a person has approved it, the agent records money moving from one
line of the plan to another as a new version, naming who approved it and
which lines it came from and went to.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Move the Money**
  - `ref/mkt/quarterly-business-review`, activity 12 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)

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
