---
name: check-duties-stay-separate
description: Reads every person's access across the finance systems against the list of duties that must stay separate, flags each person who could both prepare and approve the same thing, and reads the period's records for anything one flagged person both prepared and approved. Use it when running `ref/fin/review-access-to-finance-systems`.
license: CC-BY-4.0
metadata:
  agent: controls-tester
  agent-version: "1"
---

# Check duties stay separate

## What it does

Reads every person's access across the finance systems against the list
of duties that must stay separate, flags each person who could both
prepare and approve the same thing, and reads the period's records for
anything one flagged person both prepared and approved.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Flag Who Could Both Prepare and Approve**
  - `ref/fin/review-access-to-finance-systems`, activity 7 -
    [Review Access to Finance Systems](../../../../processes/finance/review-access-to-finance-systems.md)
- **Read the Records for Self-Approved Work**
  - `ref/fin/review-access-to-finance-systems`, activity 8 -
    [Review Access to Finance Systems](../../../../processes/finance/review-access-to-finance-systems.md)

## What to record

Each test leaves the control with its period, its owner and its last
result, the control as written with the risk it covers and the evidence
it should leave, the walkthrough and whether the control runs as
written, the sample size and the method the statistician agent set
before any item was drawn, the population and the draw recorded so
anyone can draw it again, each item passed or failed with the evidence
it rests on, and each failure written up with its cause, the items it
touched and what it could have let through. Beside them sit the
controller's rating and signed result, each fix with its owner and its
date, and each fix tested again on a new sample with its result. Each
access review leaves every person flagged with the duties their access
joins, and each journal, payment, supplier change or reconciliation one
flagged person both prepared and approved. Nothing in the record shows
this agent rating a finding, deciding a fix or a clash, closing a
finding, or testing a control it performs.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
