---
name: prepare-the-test
description: Opens each test from the control list with the control, the period, the owner and the last result, reads the control as written with the risk it covers and the evidence it should leave, and walks through one instance with the control owner to confirm it runs as written. Use it when running `ref/fin/test-a-financial-control`.
license: CC-BY-4.0
metadata:
  agent: controls-tester
  agent-version: "1"
---

# Prepare the test

## What it does

Opens each test from the control list with the control, the period, the
owner and the last result, reads the control as written with the risk it
covers and the evidence it should leave, and walks through one instance
with the control owner to confirm it runs as written.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Open the Test**
  - `ref/fin/test-a-financial-control`, activity 1 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)
- **Read the Control as Written**
  - `ref/fin/test-a-financial-control`, activity 2 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)
- **Walk Through the Control With Its Owner**
  - `ref/fin/test-a-financial-control`, activity 3 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)

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
