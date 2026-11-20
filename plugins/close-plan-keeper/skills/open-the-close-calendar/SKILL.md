---
name: open-the-close-calendar
description: Opens the calendar for closing the books each period at its version, with every task, one owner and one day on each and the quarter and year tasks where they apply, as the controller confirms it, and announces the last day for entries from each sub-ledger and each team. Use it when running `ref/fin/close-the-month`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Open the close calendar

## What it does

Opens the calendar for closing the books each period at its version,
with every task, one owner and one day on each and the quarter and year
tasks where they apply, as the controller confirms it, and announces the
last day for entries from each sub-ledger and each team.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Announce the Cutoffs**
  - `ref/fin/close-the-month`, activity 2 -
    [Close the Month](../../../../processes/finance/close-the-month.md)
- **Open the Close Calendar**
  - `ref/fin/close-the-month`, activity 1 -
    [Close the Month](../../../../processes/finance/close-the-month.md)

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
