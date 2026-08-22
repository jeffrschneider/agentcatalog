---
name: report-the-budget-position
description: The agent reports what was allocated, what has been drawn against it and what is left, for a function, a period or a single piece of work. Use it when running `ref/mkt/brand-refresh` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: budget-keeper
  agent-version: "1"
---

# Report the budget position

## What it does

The agent reports what was allocated, what has been drawn against it and
what is left, for a function, a period or a single piece of work. It
also says what can still be spent this year and in the years after.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Account for the Money**
  - `ref/mkt/brief-executive-leadership`, activity 6 -
    [Brief Executive Leadership](../../../../processes/marketing/brief-executive-leadership.md)
- **Read the Budget Position**
  - `ref/mkt/quarterly-business-review`, activity 4 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Report the Transition**
  - `ref/mkt/brand-refresh`, activity 25 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Say What Money There Is**
  - `ref/mkt/select-marketing-technology`, activity 7 -
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
