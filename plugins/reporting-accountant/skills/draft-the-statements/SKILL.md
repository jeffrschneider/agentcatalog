---
name: draft-the-statements
description: Opens the reporting pack, takes in the signed consolidated trial balance, maps each account to its line, drafts the statements, gathers the inputs to each note from their owners, drafts the notes and the tax note, revises each draft with every change marked, and hands the year-end draft to the external audit. Use it when running `ref/fin/calculate-the-tax-provision` and `ref/fin/prepare-the-financial-statements`.
license: CC-BY-4.0
metadata:
  agent: reporting-accountant
  agent-version: "1"
---

# Draft the statements

## What it does

Opens the reporting pack, takes in the signed consolidated trial
balance, maps each account to its line, drafts the statements, gathers
the inputs to each note from their owners, drafts the notes and the tax
note, revises each draft with every change marked, and hands the
year-end draft to the external audit.

## Where it happens

The agent does this in ten activities across two reference processes.
Each one names the activity as that process words it.

- **Draft the Notes**
  - `ref/fin/prepare-the-financial-statements`, activity 6 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Draft the Statements**
  - `ref/fin/prepare-the-financial-statements`, activity 4 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Draft the Tax Note**
  - `ref/fin/calculate-the-tax-provision`, activity 14 -
    [Calculate the Tax Provision](../../../../processes/finance/calculate-the-tax-provision.md)
- **Gather the Inputs to the Notes**
  - `ref/fin/prepare-the-financial-statements`, activity 5 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Hand the Draft to the Audit**
  - `ref/fin/prepare-the-financial-statements`, activity 13 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Map the Accounts to the Statements**
  - `ref/fin/prepare-the-financial-statements`, activity 3 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Open the Reporting Pack**
  - `ref/fin/prepare-the-financial-statements`, activity 1 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Record What the Period Taught**
  - `ref/fin/prepare-the-financial-statements`, activity 17 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Revise the Draft**
  - `ref/fin/prepare-the-financial-statements`, activity 12 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)
- **Take In the Consolidated Trial Balance**
  - `ref/fin/prepare-the-financial-statements`, activity 2 -
    [Prepare the Financial Statements](../../../../processes/finance/prepare-the-financial-statements.md)

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
