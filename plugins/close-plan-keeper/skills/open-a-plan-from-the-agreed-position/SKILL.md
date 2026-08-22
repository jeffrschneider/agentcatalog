---
name: open-a-plan-from-the-agreed-position
description: Takes the agreed position as it comes across from the negotiation and opens the plan on it, with the signature date both sides are working toward written at the top. Use it when running `ref/sls/negotiate-the-agreement` and `ref/sls/run-the-close-plan`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Open a plan from the agreed position

## What it does

Takes the agreed position as it comes across from the negotiation and
opens the plan on it, with the signature date both sides are working
toward written at the top.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Hand On the Agreed Position**
  - `ref/sls/negotiate-the-agreement`, activity 15 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)
- **Open the Close Plan**
  - `ref/sls/run-the-close-plan`, activity 1 -
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
