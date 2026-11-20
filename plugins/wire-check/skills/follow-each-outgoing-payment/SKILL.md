---
name: follow-each-outgoing-payment
description: Checks each payment a named person releases, such as the chief financial officer, the payroll approver or the releasers a company's delegation of authority names, against the verified line it pays, including each transfer between the company's accounts and each payroll funding, then confirms where each one landed and that each payee received it. Use it when running `ref/fin/change-a-suppliers-bank-details` and 6 other reference processes.
license: CC-BY-4.0
metadata:
  agent: wire-check
  agent-version: "1"
---

# Follow each outgoing payment

## What it does

Checks each payment a named person releases, such as the chief financial
officer, the payroll approver or the releasers a company's delegation of
authority names, against the verified line it pays, including each
transfer between the company's accounts and each payroll funding, then
confirms where each one landed and that each payee received it. It marks
the first payment to a changed account for a check, and holds a returned
or rejected payment with the bank's reason until it can be paid again to
verified details. It can see payments and holds no right to release one.

## Where it happens

The agent does this in twelve activities across seven reference
processes. Each one names the activity as that process words it.

- **Check the Funding Transfer**
  - `ref/fin/fund-the-payroll`, activity 7 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
- **Check the Payment File**
  - `ref/fin/pay-approved-invoices`, activity 9 -
    [Pay Approved Invoices](../../../../processes/finance/pay-approved-invoices.md)
  - `ref/hr/run-payroll`, activity 10 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Check the Transfer**
  - `ref/fin/move-cash-between-accounts`, activity 6 -
    [Move Cash Between Accounts](../../../../processes/finance/move-cash-between-accounts.md)
- **Confirm Each Payment Landed**
  - `ref/pc/make-a-distribution`, activity 15 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Confirm Where Each Payment Landed**
  - `ref/fin/pay-approved-invoices`, activity 11 -
    [Pay Approved Invoices](../../../../processes/finance/pay-approved-invoices.md)
- **Confirm the First Payment Landed**
  - `ref/fin/change-a-suppliers-bank-details`, activity 13 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Confirm the Funding Landed**
  - `ref/fin/fund-the-payroll`, activity 10 -
    [Fund the Payroll](../../../../processes/finance/fund-the-payroll.md)
- **Confirm the Money Arrived**
  - `ref/pc/run-the-closing`, activity 12 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **Confirm the Payments Landed**
  - `ref/hr/run-payroll`, activity 12 -
    [Run Payroll](../../../../processes/human-resources/run-payroll.md)
- **Confirm the Transfer Landed**
  - `ref/fin/move-cash-between-accounts`, activity 9 -
    [Move Cash Between Accounts](../../../../processes/finance/move-cash-between-accounts.md)
- **Handle a Returned Payment**
  - `ref/fin/pay-approved-invoices`, activity 12 -
    [Pay Approved Invoices](../../../../processes/finance/pay-approved-invoices.md)
- **Mark the First Payment**
  - `ref/fin/change-a-suppliers-bank-details`, activity 12 -
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
