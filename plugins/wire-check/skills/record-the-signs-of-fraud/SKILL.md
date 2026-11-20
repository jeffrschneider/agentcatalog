---
name: record-the-signs-of-fraud
description: Writes up a bank change the supplier does not confirm, or a first payment that did not land, as a suspected fraud for the controller the same day, with the request as it arrived, its sender and what was checked. Use it when running `ref/fin/change-a-suppliers-bank-details`.
license: CC-BY-4.0
metadata:
  agent: wire-check
  agent-version: "1"
---

# Record the signs of fraud

## What it does

Writes up a bank change the supplier does not confirm, or a first
payment that did not land, as a suspected fraud for the controller the
same day, with the request as it arrived, its sender and what was
checked. Afterwards it records the signs of fraud each change showed and
how long its confirmation took, so the next change is checked against
them.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Record What the Change Taught**
  - `ref/fin/change-a-suppliers-bank-details`, activity 15 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Report a Suspected Fraud**
  - `ref/fin/change-a-suppliers-bank-details`, activity 8 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)

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
