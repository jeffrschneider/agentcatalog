---
name: work-the-steps-that-take-the-longest
description: Runs the buyer's security review and the procurement steps as dated steps inside the plan, which means the vendor forms, the supplier setup and the order rather than a wait nobody owns. Use it when running `ref/sls/run-the-close-plan`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Work the steps that take the longest

## What it does

Runs the buyer's security review and the procurement steps as dated
steps inside the plan, which means the vendor forms, the supplier setup
and the order rather than a wait nobody owns.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Work the Procurement Steps**
  - `ref/sls/run-the-close-plan`, activity 8 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Work the Security Review**
  - `ref/sls/run-the-close-plan`, activity 7 -
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
