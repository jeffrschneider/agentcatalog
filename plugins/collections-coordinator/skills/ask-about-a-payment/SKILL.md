---
name: ask-about-a-payment
description: Asks the customer once what each held receipt or shortfall is for, and reads the answer as the invoices it paid, a deduction claimed, a payment meant for another customer or money sent in error. Use it when running `ref/fin/apply-a-customer-payment`.
license: CC-BY-4.0
metadata:
  agent: collections-coordinator
  agent-version: "1"
---

# Ask about a payment

## What it does

Asks the customer once what each held receipt or shortfall is for, and
reads the answer as the invoices it paid, a deduction claimed, a payment
meant for another customer or money sent in error.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Ask About Each Held Receipt**
  - `ref/fin/apply-a-customer-payment`, activity 8 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)
- **Read the Customer's Answer**
  - `ref/fin/apply-a-customer-payment`, activity 9 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)

## What to record

Each overdue account leaves the follow-up level it was read from, the
reminder schedule with each date, wording and contact, each reminder
sent and each reply kept against its invoice, the stage at which the
account owner was brought in and what was said, each promise with its
amount, its date, who made it and whether it was kept, each claim sent
to the dispute process with the reminders paused on its amount and
restarted after the answer, and the account as set out for a decision
with the decision and who took it. Beside them sit each change to the
reminders after the decision and each instalment of a payment plan
checked as a promise. Each held receipt leaves the one question asked
and the answer as read. Each write-off leaves everything tried and the
follow-up brought in line with the decision. Nothing in the record shows
this agent agreeing a payment plan, a settlement, a hold or an agency
handover, or adding interest or a charge on its own.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
