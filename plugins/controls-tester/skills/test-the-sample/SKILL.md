---
name: test-the-sample
description: Draws the sample from the whole period at the size the statistician agent set, with the population and the draw recorded, tests each item against the evidence the control should leave, writes up each failure with its cause, tests each fix again on a new sample, and records what the test taught. Use it when running `ref/fin/test-a-financial-control`.
license: CC-BY-4.0
metadata:
  agent: controls-tester
  agent-version: "1"
---

# Test the sample

## What it does

Draws the sample from the whole period at the size the statistician
agent set, with the population and the draw recorded, tests each item
against the evidence the control should leave, writes up each failure
with its cause, tests each fix again on a new sample, and records what
the test taught.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Draw the Sample**
  - `ref/fin/test-a-financial-control`, activity 5 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)
- **Record What the Test Taught**
  - `ref/fin/test-a-financial-control`, activity 17 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)
- **Test Each Item Against Its Evidence**
  - `ref/fin/test-a-financial-control`, activity 6 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)
- **Test the Fix Again**
  - `ref/fin/test-a-financial-control`, activity 15 -
    [Test a Financial Control](../../../../processes/finance/test-a-financial-control.md)
- **Write Up Each Failure With Its Cause**
  - `ref/fin/test-a-financial-control`, activity 7 -
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
