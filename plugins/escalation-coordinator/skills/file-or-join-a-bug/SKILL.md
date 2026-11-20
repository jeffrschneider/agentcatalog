---
name: file-or-join-a-bug
description: Joins a case to the bug already filed with its account and any new evidence, or proposes a severity from the harm, the accounts and any workaround and files a new bug with the steps, the evidence and the accounts. Use it when running `ref/sup/report-a-confirmed-bug`.
license: CC-BY-4.0
metadata:
  agent: escalation-coordinator
  agent-version: "1"
---

# File or join a bug

## What it does

Joins a case to the bug already filed with its account and any new
evidence, or proposes a severity from the harm, the accounts and any
workaround and files a new bug with the steps, the evidence and the
accounts.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **File the Bug**
  - `ref/sup/report-a-confirmed-bug`, activity 8 -
    [Report a Confirmed Bug](../../../../processes/customer-support/report-a-confirmed-bug.md)
- **Join the Case to the Bug Already Filed**
  - `ref/sup/report-a-confirmed-bug`, activity 6 -
    [Report a Confirmed Bug](../../../../processes/customer-support/report-a-confirmed-bug.md)
- **Propose the Severity**
  - `ref/sup/report-a-confirmed-bug`, activity 7 -
    [Report a Confirmed Bug](../../../../processes/customer-support/report-a-confirmed-bug.md)

## What to record

Each escalation leaves its reason, the summary at the version the first
specialist confirmed with each line traced to the case, the tier and the
named specialist chosen with the topic, the entitlement and who was
free, each tier the case passed through with what each tried, the
outcome handed back, and what the first specialist was told solved it.
Each bug report leaves the fault as reproduced, the completeness check
with anything sent back to the specialist, the evidence as masked, the
search of the bugs already filed with each likely match and why, the bug
filed or joined, the severity proposed with its reasons and the severity
engineering set, each follow-up with its answer, each change in the
picture brought to the triage lead, and the fix as taken in with every
customer and case linked to it. Each security or safety report leaves
the report exactly as it was made, who could open the case and each
opening, any request to take it out of public view, how it was sorted,
the time it was sent and the time a named person confirmed holding it,
any notice to the privacy lead and the legal team with the time the
company first knew, each follow-up, each later report joined, and the
outcome. Nothing in the record shows this agent promising a fix or a
date, setting a severity, deciding anything about a security or safety
report, or sending a word to a customer or a reporter.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
