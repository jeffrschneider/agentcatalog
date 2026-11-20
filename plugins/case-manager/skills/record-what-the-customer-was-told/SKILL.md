---
name: record-what-the-customer-was-told
description: Keeps the case beside the person who tells the customer something that matters, such as who now holds the case, what is known about a bug, a credit or a complaint's answer, and records who approved and sent it and when. Use it when running `ref/sup/answer-a-billing-question` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: case-manager
  agent-version: "1"
---

# Record what the customer was told

## What it does

Keeps the case beside the person who tells the customer something that
matters, such as who now holds the case, what is known about a bug, a
credit or a complaint's answer, and records who approved and sent it and
when.

## Where it happens

The agent does this in six activities across six reference processes.
Each one names the activity as that process words it.

- **Record the Approval on the Case**
  - `ref/sup/approve-a-sensitive-reply`, activity 13 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)
- **Send the Answer**
  - `ref/sup/answer-a-formal-complaint`, activity 14 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)
- **Tell Each Customer Its Credit**
  - `ref/sup/follow-up-an-outage`, activity 14 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)
- **Tell Each Linked Customer What Is Known**
  - `ref/sup/report-a-confirmed-bug`, activity 11 -
    [Report a Confirmed Bug](../../../../processes/customer-support/report-a-confirmed-bug.md)
- **Tell the Customer Who Holds It**
  - `ref/sup/escalate-a-case-to-a-specialist`, activity 8 -
    [Escalate a Case to a Specialist](../../../../processes/customer-support/escalate-a-case-to-a-specialist.md)
- **Tell the Customer Who Holds It Now**
  - `ref/sup/answer-a-billing-question`, activity 11 -
    [Answer a Billing Question](../../../../processes/customer-support/answer-a-billing-question.md)

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
