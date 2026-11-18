---
name: open-the-formation-checklist
description: Takes the decided strategy and the fund model in at their version and opens one formation checklist on them, listing every step the fund needs before it can take a commitment, each with one owner and one date. Use it when running `ref/pc/form-the-fund`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Open the formation checklist

## What it does

Takes the decided strategy and the fund model in at their version and
opens one formation checklist on them, listing every step the fund needs
before it can take a commitment, each with one owner and one date.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Open the Formation Checklist**
  - `ref/pc/form-the-fund`, activity 2 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Take in the Decided Strategy**
  - `ref/pc/form-the-fund`, activity 1 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)

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
