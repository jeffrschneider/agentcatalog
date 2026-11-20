---
name: reconcile-to-the-cent
description: Compares what was called or approved with what was received or paid and what was booked, investor by investor, with the capital-account-keeper agent, and agrees the bank balance to the books. Use it when running `ref/fin/fund-the-payroll`, `ref/pc/issue-a-capital-call` and `ref/pc/make-a-distribution`.
license: CC-BY-4.0
metadata:
  agent: wire-check
  agent-version: "1"
---

# Reconcile to the cent

## What it does

Compares what was called or approved with what was received or paid and
what was booked, investor by investor, with the capital-account-keeper
agent, and agrees the bank balance to the books. For a payroll funding
it sets the funding against every payment that left the payroll account
on payday.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Match the Funding to the Payments**
  - `ref/fin/fund-the-payroll`, activity 12 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
- **Reconcile the Call**
  - `ref/pc/issue-a-capital-call`, activity 16 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Reconcile the Distribution**
  - `ref/pc/make-a-distribution`, activity 17 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)

## What to record

Each instruction checked leaves the account as it was received, the
channel it came in, the contact called and where that contact's number
came from, the date, the person reached and the result, verified or
held. A change to instructions close to a closing or a pay date is
recorded as suspect until it is verified again, and a change that
arrived by email alone is recorded with the report of it as an attempted
fraud. At a closing, each payment released is recorded against the
verified line of the funds flow it pays, and each payee's receipt is
matched to its line. For a capital call, the fund's receiving account on
each notice is recorded as checked, and each receipt is matched to an
investor, a call and an amount, with anything late, short, over or from
an account not on record held aside with the reason. For a sale and a
distribution, the proceeds are recorded as cleared in the fund's account
with any escrow, holdback or later payment named, and each payment is
matched to its bank confirmation, with anything rejected or returned
held aside. Each call and distribution leaves a reconciliation of what
was called or approved, what was received or paid, and what was booked,
investor by investor, with the bank balance agreed to the books. Nothing
in the record shows this agent releasing a payment, because it holds no
right to.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
