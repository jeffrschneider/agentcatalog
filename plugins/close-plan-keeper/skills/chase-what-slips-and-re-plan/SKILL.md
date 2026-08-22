---
name: chase-what-slips-and-re-plan
description: Chases a step past its date with its owner, re-dates it with the buyer or sends it up, and moves every step behind it when a date moves. Use it when running `ref/sls/run-the-close-plan`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Chase what slips and re plan

## What it does

Chases a step past its date with its owner, re-dates it with the buyer
or sends it up, and moves every step behind it when a date moves.
Reports where the deal stands against its own plan.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Chase the Slipping Steps**
  - `ref/sls/run-the-close-plan`, activity 10 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Re-Plan When a Date Moves**
  - `ref/sls/run-the-close-plan`, activity 11 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Report the Plan**
  - `ref/sls/run-the-close-plan`, activity 12 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)

## What to record

The plan opened from the agreed position, with the signature date. Every
step, on either side, with one named owner and one date, and the steps
that block others marked. The buyer's approval path with the committee
dates and the person who takes it to each one. The buyer's confirmation
of the plan, kept and dated. Every chase, with the reason the owner gave
and the new date it produced. Every re-plan, showing which steps moved
and whether the signature date moved or the slack was named. The
pre-signature conditions marked done with their evidence. At close, the
plan with what slipped, why, and what to plan differently.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
