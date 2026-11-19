---
name: follow-each-outgoing-payment
description: Checks each payment a named person releases, such as the chief financial officer or the payroll approver, against the verified line it pays, then confirms where each one landed and that each payee received it. Use it when running `ref/hr/run-payroll`, `ref/pc/make-a-distribution` and `ref/pc/run-the-closing`.
license: CC-BY-4.0
metadata:
  agent: wire-check
  agent-version: "1"
---

# Follow each outgoing payment

## What it does

Checks each payment a named person releases, such as the chief financial
officer or the payroll approver, against the verified line it pays, then
confirms where each one landed and that each payee received it. It can
see payments and holds no right to release one.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Check the Payment File**
  - `ref/hr/run-payroll`, activity 10 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Confirm Each Payment Landed**
  - `ref/pc/make-a-distribution`, activity 15 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Confirm the Money Arrived**
  - `ref/pc/run-the-closing`, activity 12 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **Confirm the Payments Landed**
  - `ref/hr/run-payroll`, activity 12 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)

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
