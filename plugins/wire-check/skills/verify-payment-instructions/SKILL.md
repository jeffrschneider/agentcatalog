---
name: verify-payment-instructions
description: Checks each payee's account, each investor's account, each employee's account, each supplier's account and the fund's own receiving account against the verified record, and confirms any change by a call to a contact already on file, through a channel independent of the one the instruction came in. Use it when running `ref/fin/change-a-suppliers-bank-details` and 6 other reference processes.
license: CC-BY-4.0
metadata:
  agent: wire-check
  agent-version: "1"
---

# Verify payment instructions

## What it does

Checks each payee's account, each investor's account, each employee's
account, each supplier's account and the fund's own receiving account
against the verified record, and confirms any change by a call to a
contact already on file, through a channel independent of the one the
instruction came in. For a supplier it checks the request behind a new
or changed account for its channel, its sender, its timing and any sign
of fraud, sets the account name and the bank against the supplier's
legal name, and finds the contact on file, or one apart from the
request, that a person calls. An account it cannot confirm holds that
payment.

## Where it happens

The agent does this in nine activities across seven reference processes.
Each one names the activity as that process words it.

- **Check the Bank Details**
  - `ref/fin/set-up-a-supplier`, activity 8 -
    [Set Up a Supplier](../../../../processes/finance/set-up-a-supplier.md)
- **Check the New Account**
  - `ref/fin/change-a-suppliers-bank-details`, activity 5 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Check the Request**
  - `ref/fin/change-a-suppliers-bank-details`, activity 4 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Confirm a New Bank Account**
  - `ref/hr/change-an-employee-record`, activity 4 -
    [Change an Employee Record](../../../../processes/human-resources/change-an-employee-record.md)
- **Confirm the Fund's Bank Instructions**
  - `ref/pc/issue-a-capital-call`, activity 9 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Find a Contact Apart from the Request**
  - `ref/fin/set-up-a-supplier`, activity 9 -
    [Set Up a Supplier](../../../../processes/finance/set-up-a-supplier.md)
- **Find the Contact on File**
  - `ref/fin/change-a-suppliers-bank-details`, activity 6 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Verify Each Investor's Payment Instructions**
  - `ref/pc/make-a-distribution`, activity 13 -
    [Make a Distribution](../../../../processes/private-capital/make-a-distribution.md)
- **Verify the Payment Instructions**
  - `ref/pc/allocate-fees-and-expenses`, activity 15 -
    [Allocate Fees and Expenses](../../../../processes/private-capital/allocate-fees-and-expenses.md)
  - `ref/pc/run-the-closing`, activity 8 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)

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
