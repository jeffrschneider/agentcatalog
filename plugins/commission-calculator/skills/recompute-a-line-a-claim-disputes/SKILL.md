---
name: recompute-a-line-a-claim-disputes
description: Freezes the statement at the version the claimant holds, pulls the records the number was computed from, and computes the line again independently from those same records. Use it when running `ref/rev/settle-a-commission-dispute`.
license: CC-BY-4.0
metadata:
  agent: commission-calculator
  agent-version: "1"
---

# Recompute a line a claim disputes

## What it does

Freezes the statement at the version the claimant holds, pulls the
records the number was computed from, and computes the line again
independently from those same records. Where the claim is upheld, the
correction lands in the next run as its own line and the cause goes back
to whoever owns it.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Correct the Statement and the Next Run**
  - `ref/rev/settle-a-commission-dispute`, activity 13 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Feed the Cause Back**
  - `ref/rev/settle-a-commission-dispute`, activity 15 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Freeze the Statement Version**
  - `ref/rev/settle-a-commission-dispute`, activity 4 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Pull the Evidence Behind the Line**
  - `ref/rev/settle-a-commission-dispute`, activity 5 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)
- **Recompute the Line Independently**
  - `ref/rev/settle-a-commission-dispute`, activity 6 -
    [Settle a Commission Dispute](../../../../processes/revenue-operations/settle-a-commission-dispute.md)

## What to record

Per run: the period boundaries, the sellers in scope, the plan version
each seller sits on, and the booking snapshot with the system, the query
and the timestamp it was taken at. Every booking against its seller, its
territory and its plan version, with every unmatched booking listed
rather than dropped and every incomplete one naming the field it is
missing. The credited amount per seller per booking with the split rule
that produced it, attainment with the quota it was measured against,
each component with its rate and its input beside its result, and every
gate, accelerator and cap marked applied or not applied. Every draw,
recoverable and clawback with the period it came from, and every held
amount with the condition it waits on and the period it is expected in.
Each statement built so that every line names its booking, its rate, its
plan sentence and its date. Then what each manager accepted and what
they said was wrong, the run at a version with its total and its
signatures, what payroll received and when, and every correction with
the plan sentence or the record that caused it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
