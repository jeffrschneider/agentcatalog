---
name: route-a-dispute
description: Sends each claim that an invoice is wrong, and each deduction a customer claims, to the dispute process in the customer's own words, pauses the reminders on the amount claimed, and restarts them on what is still owed once the answer is given. Use it when running `ref/fin/apply-a-customer-payment`, `ref/fin/collect-an-overdue-invoice` and `ref/fin/resolve-a-billing-dispute`.
license: CC-BY-4.0
metadata:
  agent: collections-coordinator
  agent-version: "1"
---

# Route a dispute

## What it does

Sends each claim that an invoice is wrong, and each deduction a customer
claims, to the dispute process in the customer's own words, pauses the
reminders on the amount claimed, and restarts them on what is still owed
once the answer is given.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Pause Collection on the Amount Claimed**
  - `ref/fin/resolve-a-billing-dispute`, activity 5 -
    [Resolve a Billing Dispute](../../../../processes/finance/resolve-a-billing-dispute.md)
- **Restart Collection on What Is Owed**
  - `ref/fin/resolve-a-billing-dispute`, activity 15 -
    [Resolve a Billing Dispute](../../../../processes/finance/resolve-a-billing-dispute.md)
- **Send a Claimed Deduction to Its Own Process**
  - `ref/fin/apply-a-customer-payment`, activity 10 -
    [Apply a Customer Payment](../../../../processes/finance/apply-a-customer-payment.md)
- **Send a Dispute to Its Own Process**
  - `ref/fin/collect-an-overdue-invoice`, activity 9 -
    [Collect an Overdue Invoice](../../../../processes/finance/collect-an-overdue-invoice.md)

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
