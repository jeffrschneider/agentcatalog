---
name: carry-a-fix-back
description: Hands over each bug marked fixed with its linked cases, takes in the fix with the version and the plans it reached, lists every customer and case linked to it with who has the fix, and takes back a reply that says the fix did not help as a case of its own. Use it when running `ref/sup/report-a-confirmed-bug` and `ref/sup/tell-customers-about-a-fix`.
license: CC-BY-4.0
metadata:
  agent: escalation-coordinator
  agent-version: "1"
---

# Carry a fix back

## What it does

Hands over each bug marked fixed with its linked cases, takes in the fix
with the version and the plans it reached, lists every customer and case
linked to it with who has the fix, and takes back a reply that says the
fix did not help as a case of its own.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Hand Over the Fixed Bug**
  - `ref/sup/report-a-confirmed-bug`, activity 16 -
    [Report a Confirmed Bug](../../../../processes/customer-support/report-a-confirmed-bug.md)
- **List the Customers Linked to the Bug**
  - `ref/sup/tell-customers-about-a-fix`, activity 3 -
    [Tell Customers about a Fix](../../../../processes/customer-support/tell-customers-about-a-fix.md)
- **Take Back a Fix That Did Not Help**
  - `ref/sup/tell-customers-about-a-fix`, activity 11 -
    [Tell Customers about a Fix](../../../../processes/customer-support/tell-customers-about-a-fix.md)
- **Take In a Fixed Bug**
  - `ref/sup/tell-customers-about-a-fix`, activity 1 -
    [Tell Customers about a Fix](../../../../processes/customer-support/tell-customers-about-a-fix.md)

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
