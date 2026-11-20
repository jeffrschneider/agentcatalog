---
name: close-the-audit
description: Tracks each adjustment the auditor proposes for the named people who decide it, prepares the representation letter with each statement traced to its source, receives and files the signed opinion, drafts the answer to each point in the auditor's letter as the controller agrees it, and records what the audit taught. Use it when running `ref/fin/run-the-external-audit`.
license: CC-BY-4.0
metadata:
  agent: audit-coordinator
  agent-version: "1"
---

# Close the audit

## What it does

Tracks each adjustment the auditor proposes for the named people who
decide it, prepares the representation letter with each statement traced
to its source, receives and files the signed opinion, drafts the answer
to each point in the auditor's letter as the controller agrees it, and
records what the audit taught.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Agree the Response to the Auditor's Letter**
  - `ref/fin/run-the-external-audit`, activity 18 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
- **Prepare the Representation Letter**
  - `ref/fin/run-the-external-audit`, activity 15 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
- **Receive the Auditor's Opinion**
  - `ref/fin/run-the-external-audit`, activity 17 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
- **Record What the Audit Taught**
  - `ref/fin/run-the-external-audit`, activity 20 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
- **Track Each Proposed Adjustment**
  - `ref/fin/run-the-external-audit`, activity 12 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)

## What to record

Each audit leaves the year, the entities in scope, the auditor and the
signed engagement letter, last year's letter with the state of each fix,
and the plan, the timetable and the materiality as agreed. Beside them
sit the numbered request list with each request's owner, due date and
state, each answer with the check that tied it to the ledger, the
controller's approval and the log of what went, when, to whom and at
which version, and each answer held with the difference named. The
adjustment list keeps each proposed adjustment and each difference with
its amount, its accounts, its period and its effect, beside the decision
on it, who made it and why, and the differences told to the audit
committee. The run closes with the representation letter traced
statement by statement to the person who confirmed it and signed by the
named officers, the auditor's signed opinion filed with the statements,
and the company's answer to each point in the auditor's letter with its
fix, its owner and its date. Nothing in the record shows this agent
approving an answer, deciding an adjustment, signing the letter, or
sending anything beyond what a request asked for.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
