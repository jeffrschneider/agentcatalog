---
name: gather-the-case
description: Gathers the account, the case history, the customer's past cases, the replies, the steps tried and the promises, and sets them beside the person who must decide or send. Use it when running `ref/sup/answer-a-formal-complaint` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: case-manager
  agent-version: "1"
---

# Gather the case

## What it does

Gathers the account, the case history, the customer's past cases, the
replies, the steps tried and the promises, and sets them beside the
person who must decide or send.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Gather the Case History and the Records**
  - `ref/sup/answer-a-formal-complaint`, activity 7 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)
- **Gather the Case as It Stands**
  - `ref/sup/escalate-a-case-to-a-specialist`, activity 2 -
    [Escalate a Case to a Specialist](../../../../processes/customer-support/escalate-a-case-to-a-specialist.md)
- **Gather the Customer's Records**
  - `ref/sup/resolve-a-case`, activity 2 -
    [Resolve a Case](../../../../processes/customer-support/resolve-a-case.md)
- **Set the Case Beside the Reply**
  - `ref/sup/approve-a-sensitive-reply`, activity 3 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)

## What to record

Each case leaves its one owner at each point with the date it moved and
why, its state and its clock from the customer's first request, the
records gathered with where each was read, each identity check asked for
with the level it needed, the result and when the pass lapsed, each
promise with who made it, its date and whether it was kept or handed on,
each reminder sent before a date and each promise that passed, each
process it was handed to with the customer's own words and the reference
there, each reply's approver and the version sent where a named person
approved it, what each customer was told and by whom, and its close, any
reopening and the survey started. Each billing question leaves how it
was sorted, the claim or the request sent on, and the date Finance
promised with each time it was raised. Each linked bug or incident
leaves every case linked to it with its next update, and each case
closed or kept open with its reason after an outage. Each account signal
leaves the customer's own words, the kind it was sorted as and who
confirmed it, any risk or opening Sales already held, the reference in
Sales and the date, and what Sales decided with any fix a save plan
names for support. Nothing in the record shows this agent sending a
reply, deciding an answer, deciding a refund, a credit or a dispute,
making an offer or discussing a price, or scoring a support specialist.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
