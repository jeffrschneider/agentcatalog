---
name: answer-the-authority
description: Checks a notice line by line against what was filed and paid, supplies the figures and records for each audit answer, drafts the response in the form the authority asks for with each figure traced, and sets out each correction for the return's own process. Use it when running `ref/fin/respond-to-a-tax-audit` and `ref/fin/respond-to-a-tax-notice`.
license: CC-BY-4.0
metadata:
  agent: tax-analyst
  agent-version: "1"
---

# Answer the authority

## What it does

Checks a notice line by line against what was filed and paid, supplies
the figures and records for each audit answer, drafts the response in
the form the authority asks for with each figure traced, and sets out
each correction for the return's own process.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Notice Against the Return**
  - `ref/fin/respond-to-a-tax-notice`, activity 5 -
    [Respond to a Tax Notice](../../../../processes/finance/respond-to-a-tax-notice.md)
- **Correct the Return**
  - `ref/fin/respond-to-a-tax-notice`, activity 14 -
    [Respond to a Tax Notice](../../../../processes/finance/respond-to-a-tax-notice.md)
- **Draft the Answers**
  - `ref/fin/respond-to-a-tax-audit`, activity 10 -
    [Respond to a Tax Audit](../../../../processes/finance/respond-to-a-tax-audit.md)
- **Draft the Response**
  - `ref/fin/respond-to-a-tax-notice`, activity 8 -
    [Respond to a Tax Notice](../../../../processes/finance/respond-to-a-tax-notice.md)

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
