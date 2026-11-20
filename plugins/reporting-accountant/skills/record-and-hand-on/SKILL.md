---
name: record-and-hand-on
description: Records each sign-off with the version signed, who signed it and when, and hands the closed books and the group figures to the processes that read them, including each entity's results before tax for the tax provision and the closed figures for the covenant tests. Use it when running `ref/fin/calculate-the-tax-provision` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: reporting-accountant
  agent-version: "1"
---

# Record and hand on

## What it does

Records each sign-off with the version signed, who signed it and when,
and hands the closed books and the group figures to the processes that
read them, including each entity's results before tax for the tax
provision and the closed figures for the covenant tests.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Hand On the Closed Books**
  - `ref/fin/close-the-month`, activity 14 -
    [Close the Month](../../../../processes/finance/close-the-month.md)
- **Hand On the Group Figures**
  - `ref/fin/consolidate-the-group-accounts`, activity 15 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Record the Sign-Off**
  - `ref/fin/close-the-month`, activity 13 -
    [Close the Month](../../../../processes/finance/close-the-month.md)
  - `ref/fin/prepare-the-financial-statements`, activity 15 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Supply the Results Before Tax**
  - `ref/fin/calculate-the-tax-provision`, activity 1 -
    [Calculate the Tax Provision](../../../../processes/finance/calculate-the-tax-provision.md)
- **Take In the Closed Figures**
  - `ref/fin/check-the-debt-covenants`, activity 3 -
    [Check the Debt Covenants](../../../../processes/finance/check-the-debt-covenants.md)

## What to record

Each monthly close leaves each account in each entity beside the last
period, each movement above the threshold flagged with its owner's
explanation and evidence, the version of the close the controller signed
off with who signed it and when, and each entity's closed trial balance
as it was handed on. Each consolidation leaves the entities in the group
and the share owned of each, each entity's trial balance as its entity
controller signed it off, each mapping to the group chart, each rate
with its date and its source, each translation with the difference
carried to its reserve, the eliminations and the group entries with
their support and their approval, the consolidated trial balance at its
version, each group figure beside the last period with each movement
traced, the group controller's sign-off, and the posted tax agreed to
the approved provision. Each set of statements leaves the timetable and
the framework at their versions, each account mapped to its line, each
version of the statements and the notes with the source of every figure,
each note's inputs with its owner's confirmation, the disclosure check,
every figure beside the last period, the tie-out, each review point and
decision with the version that answered it, and the signing officers'
sign-off with the version they read. Nothing in the record shows this
agent approving a group entry, signing off a close, a consolidation or a
set of statements, or releasing anything outside the company.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
