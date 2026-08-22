---
name: name-the-steps-and-put-an-owner-and-a-date-on-each
description: Lists every step still owed as one set rather than two, walks the buyer's own approval path committee by committee, puts one named owner on each step and counts the dates back from signing. Use it when running `ref/sls/run-the-close-plan`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Name the steps and put an owner and a date on each

## What it does

Lists every step still owed as one set rather than two, walks the
buyer's own approval path committee by committee, puts one named owner
on each step and counts the dates back from signing.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Confirm the Buyer's Own Process**
  - `ref/sls/run-the-close-plan`, activity 3 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Date Every Step**
  - `ref/sls/run-the-close-plan`, activity 5 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Name the Steps Each Side Owes**
  - `ref/sls/run-the-close-plan`, activity 2 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Put an Owner on Every Step**
  - `ref/sls/run-the-close-plan`, activity 4 -
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
