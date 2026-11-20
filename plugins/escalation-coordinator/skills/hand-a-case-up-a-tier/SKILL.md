---
name: hand-a-case-up-a-tier
description: Takes in each escalation, writes one summary of the problem, the steps tried and what the customer was told, chooses the tier and a named specialist, sends a case one tier up when this tier cannot resolve it, hands the outcome back, and tells the first specialist what solved it. Use it when running `ref/sup/escalate-a-case-to-a-specialist`.
license: CC-BY-4.0
metadata:
  agent: escalation-coordinator
  agent-version: "1"
---

# Hand a case up a tier

## What it does

Takes in each escalation, writes one summary of the problem, the steps
tried and what the customer was told, chooses the tier and a named
specialist, sends a case one tier up when this tier cannot resolve it,
hands the outcome back, and tells the first specialist what solved it.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Choose the Tier and the Specialist**
  - `ref/sup/escalate-a-case-to-a-specialist`, activity 5 -
    [Escalate a Case to a Specialist](../../../../processes/customer-support/escalate-a-case-to-a-specialist.md)
- **Escalate to the Next Tier**
  - `ref/sup/escalate-a-case-to-a-specialist`, activity 13 -
    [Escalate a Case to a Specialist](../../../../processes/customer-support/escalate-a-case-to-a-specialist.md)
- **Hand the Outcome Back**
  - `ref/sup/escalate-a-case-to-a-specialist`, activity 14 -
    [Escalate a Case to a Specialist](../../../../processes/customer-support/escalate-a-case-to-a-specialist.md)
- **Take In the Escalation**
  - `ref/sup/escalate-a-case-to-a-specialist`, activity 1 -
    [Escalate a Case to a Specialist](../../../../processes/customer-support/escalate-a-case-to-a-specialist.md)
- **Tell the First Specialist What Solved It**
  - `ref/sup/escalate-a-case-to-a-specialist`, activity 15 -
    [Escalate a Case to a Specialist](../../../../processes/customer-support/escalate-a-case-to-a-specialist.md)
- **Write the Escalation Summary**
  - `ref/sup/escalate-a-case-to-a-specialist`, activity 3 -
    [Escalate a Case to a Specialist](../../../../processes/customer-support/escalate-a-case-to-a-specialist.md)

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
