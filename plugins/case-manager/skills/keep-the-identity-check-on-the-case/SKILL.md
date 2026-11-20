---
name: keep-the-identity-check-on-the-case
description: Sends each action that would read out or change anything in the account to the identity check, records the result with the level reached, holds a possible takeover with the account untouched, and ends the pass when the case closes or its window runs out. Use it when running `ref/sup/answer-a-billing-question` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: case-manager
  agent-version: "1"
---

# Keep the identity check on the case

## What it does

Sends each action that would read out or change anything in the account
to the identity check, records the result with the level reached, holds
a possible takeover with the account untouched, and ends the pass when
the case closes or its window runs out.

## Where it happens

The agent does this in seven activities across four reference processes.
Each one names the activity as that process words it.

- **Confirm the Asker Was Verified**
  - `ref/sup/answer-a-billing-question`, activity 2 -
    [Answer a Billing Question](../../../../processes/customer-support/answer-a-billing-question.md)
- **Confirm the Person Where the Case Needs It**
  - `ref/sup/resolve-a-case`, activity 3 -
    [Resolve a Case](../../../../processes/customer-support/resolve-a-case.md)
- **Hold a Possible Takeover**
  - `ref/sup/verify-a-customers-identity`, activity 8 -
    [Verify a Customer's Identity](../../../../processes/customer-support/verify-a-customers-identity.md)
- **Let the Result Lapse**
  - `ref/sup/verify-a-customers-identity`, activity 13 -
    [Verify a Customer's Identity](../../../../processes/customer-support/verify-a-customers-identity.md)
- **Record the Result on the Case**
  - `ref/sup/verify-a-customers-identity`, activity 7 -
    [Verify a Customer's Identity](../../../../processes/customer-support/verify-a-customers-identity.md)
- **Start the Identity Check Where Needed**
  - `ref/sup/answer-a-routine-question`, activity 5 -
    [Answer a Routine Question](../../../../processes/customer-support/answer-a-routine-question.md)
- **Take In the Action Asked For**
  - `ref/sup/verify-a-customers-identity`, activity 1 -
    [Verify a Customer's Identity](../../../../processes/customer-support/verify-a-customers-identity.md)

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
