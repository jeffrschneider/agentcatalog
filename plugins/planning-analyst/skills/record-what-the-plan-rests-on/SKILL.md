---
name: record-what-the-plan-rests-on
description: Records what each budget, reforecast and case rests on, how the last forecast compared with what happened, and what the next run checks first. Use it when running `ref/fin/approve-an-investment-case`, `ref/fin/reforecast-the-year` and `ref/fin/set-the-annual-budget`.
license: CC-BY-4.0
metadata:
  agent: planning-analyst
  agent-version: "1"
---

# Record what the plan rests on

## What it does

Records what each budget, reforecast and case rests on, how the last
forecast compared with what happened, and what the next run checks
first.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Record What the Budget Rests On**
  - `ref/fin/set-the-annual-budget`, activity 18 -
    [Set the Annual Budget](../../../../processes/finance/set-the-annual-budget.md)
- **Record What the Case Rests On**
  - `ref/fin/approve-an-investment-case`, activity 18 -
    [Approve an Investment Case](../../../../processes/finance/approve-an-investment-case.md)
- **Record What the Reforecast Rests On**
  - `ref/fin/reforecast-the-year`, activity 17 -
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
