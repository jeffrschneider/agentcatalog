---
name: consolidate-the-group
description: Opens each consolidation with the entities and the share owned of each, takes in each entity's signed-off trial balance, maps each local account to the group chart, sets the dated rates, translates each entity into the group currency, prepares the eliminations and the other group entries, builds the consolidated trial balance once they are approved, and brings the posted tax into it. Use it when running `ref/fin/calculate-the-tax-provision` and `ref/fin/consolidate-the-group-accounts`.
license: CC-BY-4.0
metadata:
  agent: reporting-accountant
  agent-version: "1"
---

# Consolidate the group

## What it does

Opens each consolidation with the entities and the share owned of each,
takes in each entity's signed-off trial balance, maps each local account
to the group chart, sets the dated rates, translates each entity into
the group currency, prepares the eliminations and the other group
entries, builds the consolidated trial balance once they are approved,
and brings the posted tax into it.

## Where it happens

The agent does this in ten activities across two reference processes.
Each one names the activity as that process words it.

- **Bring the Tax Into the Group Accounts**
  - `ref/fin/calculate-the-tax-provision`, activity 13 -
    [Calculate the Tax Provision](../../../../processes/finance/calculate-the-tax-provision.md)
- **Build the Consolidated Trial Balance**
  - `ref/fin/consolidate-the-group-accounts`, activity 12 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Map Each Entity to the Group Chart**
  - `ref/fin/consolidate-the-group-accounts`, activity 3 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Open the Consolidation**
  - `ref/fin/consolidate-the-group-accounts`, activity 1 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Prepare the Eliminations**
  - `ref/fin/consolidate-the-group-accounts`, activity 9 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Prepare the Other Group Entries**
  - `ref/fin/consolidate-the-group-accounts`, activity 10 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Record What the Consolidation Taught**
  - `ref/fin/consolidate-the-group-accounts`, activity 16 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Set the Exchange Rates**
  - `ref/fin/consolidate-the-group-accounts`, activity 4 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Take In Each Entity's Trial Balance**
  - `ref/fin/consolidate-the-group-accounts`, activity 2 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)
- **Translate Into the Group Currency**
  - `ref/fin/consolidate-the-group-accounts`, activity 5 -
    [Consolidate the Group Accounts](../../../../processes/finance/consolidate-the-group-accounts.md)

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
