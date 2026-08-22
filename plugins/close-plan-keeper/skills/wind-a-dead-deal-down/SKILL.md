---
name: wind-a-dead-deal-down
description: Stops the trials, pilots and pending approvals when a deal is called lost, and gives back or deletes what the buyer gave us. Use it when running `ref/sls/record-a-lost-deal`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Wind a dead deal down

## What it does

Stops the trials, pilots and pending approvals when a deal is called
lost, and gives back or deletes what the buyer gave us.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Return the Buyer's Material**
  - `ref/sls/record-a-lost-deal`, activity 10 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)
- **Stop the Open Work**
  - `ref/sls/record-a-lost-deal`, activity 9 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)

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
