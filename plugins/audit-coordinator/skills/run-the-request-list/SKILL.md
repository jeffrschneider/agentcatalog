---
name: run-the-request-list
description: Opens the audit with its scope and last year's letter, keeps the auditor's requests on one numbered list with an owner and a due date for each, sends each request to whoever holds the answer, checks each answer against the ledger and the request before it goes, and sends and logs each approved answer. Use it when running `ref/fin/run-the-external-audit`.
license: CC-BY-4.0
metadata:
  agent: audit-coordinator
  agent-version: "1"
---

# Run the request list

## What it does

Opens the audit with its scope and last year's letter, keeps the
auditor's requests on one numbered list with an owner and a due date for
each, sends each request to whoever holds the answer, checks each answer
against the ledger and the request before it goes, and sends and logs
each approved answer.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Check Each Answer Before It Goes**
  - `ref/fin/run-the-external-audit`, activity 9 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
- **Log the Request List**
  - `ref/fin/run-the-external-audit`, activity 3 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
- **Open the Audit**
  - `ref/fin/run-the-external-audit`, activity 1 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
- **Send Each Request to Its Owner**
  - `ref/fin/run-the-external-audit`, activity 4 -
    [Run the External Audit](../../../../processes/finance/run-the-external-audit.md)
- **Send the Answers and Log Them**
  - `ref/fin/run-the-external-audit`, activity 11 -
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
