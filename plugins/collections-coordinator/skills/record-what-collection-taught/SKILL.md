---
name: record-what-collection-taught
description: Records which reminders brought payment, which promises were broken, which warning signs came first, and what the follow-up level for the customer should be. Use it when running `ref/fin/collect-an-overdue-invoice` and `ref/fin/write-off-a-bad-debt`.
license: CC-BY-4.0
metadata:
  agent: collections-coordinator
  agent-version: "1"
---

# Record what collection taught

## What it does

Records which reminders brought payment, which promises were broken,
which warning signs came first, and what the follow-up level for the
customer should be.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Record What the Debt Taught**
  - `ref/fin/write-off-a-bad-debt`, activity 16 -
    [Write Off a Bad Debt](../../../../processes/finance/write-off-a-bad-debt.md)
- **Record What the Run Taught**
  - `ref/fin/collect-an-overdue-invoice`, activity 16 -
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
