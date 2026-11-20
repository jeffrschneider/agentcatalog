---
name: confirm-the-rules
description: Reads the rates, the rules and the form for each period or year against the last provision or return under the rules of each jurisdiction, and asks the head of tax to confirm each change before anything is worked out on it. Use it when running `ref/fin/calculate-the-tax-provision`, `ref/fin/file-an-indirect-tax-return` and `ref/fin/file-the-income-tax-return`.
license: CC-BY-4.0
metadata:
  agent: tax-analyst
  agent-version: "1"
---

# Confirm the rules

## What it does

Reads the rates, the rules and the form for each period or year against
the last provision or return under the rules of each jurisdiction, and
asks the head of tax to confirm each change before anything is worked
out on it.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Confirm the Rates and Rules**
  - `ref/fin/calculate-the-tax-provision`, activity 2 -
    [Calculate the Tax Provision](../../../../processes/finance/calculate-the-tax-provision.md)
- **Confirm the Rules for the Period**
  - `ref/fin/file-an-indirect-tax-return`, activity 2 -
    [File an Indirect Tax Return](../../../../processes/finance/file-an-indirect-tax-return.md)
- **Confirm the Rules for the Year**
  - `ref/fin/file-the-income-tax-return`, activity 3 -
    [File the Income Tax Return](../../../../processes/finance/file-the-income-tax-return.md)

## What to record

Each run leaves the rates, rules and form confirmed by the head of tax
for its period or year, every line gathered with its source and the
data-quality-check agent's result, and the workpapers at their versions.
Each indirect tax return leaves the tax on sales by rate and
jurisdiction, the tax on purchases with each line the rules exclude,
each open treatment set out beside the position the head of tax took,
the reconciliation to the ledger and the comparison with the last return
with every difference explained, and the payment as it was set out for
the approver. Each provision leaves each difference carried in from a
filed return, each item the rules treat differently, the current and the
deferred tax by entity and jurisdiction, each judgment set out beside
its decision, the reconciliation to the headline rate, each movement
from the last period explained, the head of tax's approval and the entry
handed to the ledger. Each income tax return leaves the signed accounts
and the provision it started from, the schedules, each adjustment to
taxable income traced to the accounts and the rule, each position set
out beside the decision, the tax due, the comparison with the provision
and the last return, and the adjustment posted and carried into the next
provision. Each notice and audit leaves the authority's figures set
against what was filed and paid, the records pulled and those held back
with the reason, the options and each adjustment set out with the tax,
interest and penalty at stake, the response as drafted, the settlement
set out, and any correction sent to the return's own process. Nothing in
the record shows this agent taking a position, approving a provision,
signing or filing a return, or approving or releasing a payment.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
