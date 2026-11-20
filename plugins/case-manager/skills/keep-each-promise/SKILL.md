---
name: keep-each-promise
description: Records each promise made to the customer, by a reply, a sensitive reply, an outage summary or a complaint's answer, with its owner and its date, keeps each linked case open with its next update due, and raises each promise before its date passes. Use it when running `ref/sup/answer-a-billing-question` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: case-manager
  agent-version: "1"
---

# Keep each promise

## What it does

Records each promise made to the customer, by a reply, a sensitive
reply, an outage summary or a complaint's answer, with its owner and its
date, keeps each linked case open with its next update due, and raises
each promise before its date passes.

## Where it happens

The agent does this in seven activities across six reference processes.
Each one names the activity as that process words it.

- **Keep the Case Open Until Finance Answers**
  - `ref/sup/answer-a-billing-question`, activity 13 -
    [Answer a Billing Question](../../../../processes/customer-support/answer-a-billing-question.md)
- **Keep the Linked Customers Updated**
  - `ref/sup/report-a-confirmed-bug`, activity 14 -
    [Report a Confirmed Bug](../../../../processes/customer-support/report-a-confirmed-bug.md)
- **Keep the Promises the Answer Makes**
  - `ref/sup/answer-a-formal-complaint`, activity 15 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)
- **Raise a Promise Before Its Date**
  - `ref/sup/resolve-a-case`, activity 10 -
    [Resolve a Case](../../../../processes/customer-support/resolve-a-case.md)
- **Record Each Promise with Its Date**
  - `ref/sup/resolve-a-case`, activity 9 -
    [Resolve a Case](../../../../processes/customer-support/resolve-a-case.md)
- **Record What the Reply Commits To**
  - `ref/sup/approve-a-sensitive-reply`, activity 14 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)
- **Record the Promises the Summary Makes**
  - `ref/sup/follow-up-an-outage`, activity 9 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)

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
