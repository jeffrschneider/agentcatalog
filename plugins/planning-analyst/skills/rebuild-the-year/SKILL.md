---
name: rebuild-the-year
description: Rebuilds each line for the months left, explains every movement from the last forecast above the threshold, sets the year beside the budget, takes each owner's confirmation and tells each owner what changed. Use it when running `ref/fin/reforecast-the-year`.
license: CC-BY-4.0
metadata:
  agent: planning-analyst
  agent-version: "1"
---

# Rebuild the year

## What it does

Rebuilds each line for the months left, explains every movement from the
last forecast above the threshold, sets the year beside the budget,
takes each owner's confirmation and tells each owner what changed.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Confirm Each Owner's Lines**
  - `ref/fin/reforecast-the-year`, activity 10 -
    [Reforecast the Year](../../../../processes/finance/reforecast-the-year.md)
- **Explain Each Movement**
  - `ref/fin/reforecast-the-year`, activity 8 -
    [Reforecast the Year](../../../../processes/finance/reforecast-the-year.md)
- **Rebuild the Rest of the Year**
  - `ref/fin/reforecast-the-year`, activity 7 -
    [Reforecast the Year](../../../../processes/finance/reforecast-the-year.md)
- **Set the Year beside the Budget**
  - `ref/fin/reforecast-the-year`, activity 9 -
    [Reforecast the Year](../../../../processes/finance/reforecast-the-year.md)
- **Tell the Budget Owners What Changed**
  - `ref/fin/reforecast-the-year`, activity 15 -
    [Reforecast the Year](../../../../processes/finance/reforecast-the-year.md)

## What to record

Each budget leaves the year, its calendar and its approvers, the
company's targets at their version, each assumption with its source and
the CFO's agreement, the instructions each department head received,
each draft at its version with the check beside it and every gap sent
back, the combined budget by month and by entity, the gap to each target
with the lines behind it, and the options with what each one gives up.
Each reforecast leaves its inputs at their versions, each owner's
changes with their evidence, the months left rebuilt with any changed
assumption marked, every movement above the threshold with its cause or
marked as unexplained, the year beside the budget, and each owner's
confirmation or correction. Each month leaves the results tied to the
trial balance, each line beside the budget and the forecast, each marked
difference with the owner who answers for it, each explanation checked
against the entries with any the entries do not support marked, the
answers to the leaders' questions, and the differences handed to the
next reforecast. Each investment case leaves the costs with their
sources, each assumption marked as supported, the sponsor's estimate or
unsourced, the risks, the funding and the case at its version. Each run
closes with what it rests on and what the next one checks first. Nothing
in the record shows this agent approving a budget, a reforecast or a
case, or writing a cause or a figure nobody gave.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
