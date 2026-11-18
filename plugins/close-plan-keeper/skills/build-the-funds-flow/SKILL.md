---
name: build-the-funds-flow
description: Builds one funds flow for a closing with every payment, payee, amount and account on it, beside the cap-table-keeper agent, so that a payment the sheet does not carry is never made. Use it when running `ref/pc/run-the-closing`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Build the funds flow

## What it does

Builds one funds flow for a closing with every payment, payee, amount
and account on it, beside the cap-table-keeper agent, so that a payment
the sheet does not carry is never made. Each line goes to the wire-check
agent to be verified, and this agent releases no money.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Build the Funds Flow**
  - `ref/pc/run-the-closing`, activity 7 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)

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
