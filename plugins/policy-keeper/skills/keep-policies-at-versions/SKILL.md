---
name: keep-policies-at-versions
description: Takes in each request with the decision behind it, reads the current version, who each variant covers and the exceptions granted under it, publishes each variant at its version with its effective date, files the published delegation of authority beside the finance policies, and keeps the old version with the dates it applied. Use it when running `ref/fin/publish-a-finance-policy` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: policy-keeper
  agent-version: "1"
---

# Keep policies at versions

## What it does

Takes in each request with the decision behind it, reads the current
version, who each variant covers and the exceptions granted under it,
publishes each variant at its version with its effective date, files the
published delegation of authority beside the finance policies, and keeps
the old version with the dates it applied. It marks every answer, form,
page, check and system rule that rests on the old version and records
the publication.

## Where it happens

The agent does this in ten activities across four reference processes.
Each one names the activity as that process words it.

- **File It With the Finance Policies**
  - `ref/fin/publish-the-delegation-of-authority`, activity 12 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
- **Keep the Old Version With Its Dates**
  - `ref/fin/publish-a-finance-policy`, activity 16 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)
  - `ref/fin/publish-the-delegation-of-authority`, activity 17 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
  - `ref/hr/publish-an-hr-policy`, activity 14 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Mark What Rests on the Old Levels**
  - `ref/sup/set-a-service-level-policy`, activity 14 -
    [Set a Service Level Policy](../../../../processes/customer-support/set-a-service-level-policy.md)
- **Mark What Rests on the Old Version**
  - `ref/fin/publish-a-finance-policy`, activity 15 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)
  - `ref/fin/publish-the-delegation-of-authority`, activity 13 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
  - `ref/hr/publish-an-hr-policy`, activity 13 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Publish the Policy at a Version**
  - `ref/fin/publish-a-finance-policy`, activity 12 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)
  - `ref/hr/publish-an-hr-policy`, activity 9 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
  - `ref/sup/set-a-service-level-policy`, activity 13 -
    [Set a Service Level Policy](../../../../processes/customer-support/set-a-service-level-policy.md)
- **Read the Current Version**
  - `ref/fin/publish-a-finance-policy`, activity 2 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)
  - `ref/hr/publish-an-hr-policy`, activity 2 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Read the Exceptions Granted Under It**
  - `ref/fin/publish-a-finance-policy`, activity 3 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)
- **Read the Policy in Force**
  - `ref/sup/set-a-service-level-policy`, activity 2 -
    [Set a Service Level Policy](../../../../processes/customer-support/set-a-service-level-policy.md)
- **Record the Publication**
  - `ref/fin/publish-a-finance-policy`, activity 17 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)
  - `ref/hr/publish-an-hr-policy`, activity 15 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Take in the Policy Request**
  - `ref/fin/publish-a-finance-policy`, activity 1 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)
  - `ref/hr/publish-an-hr-policy`, activity 1 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)

## What to record

Each change leaves the request with the decision, the confirmed rule
change or the audit finding behind it, the current version and the
people each variant covers, the draft with every change marked, each
location's variant with the blanks left for counsel, the approvers'
signatures, each variant published at its version with its effective
date, what each person was sent and when, each person's acknowledgment
of the version they were sent, every answer, form and page marked as
resting on the old version, and the old version closed with the dates it
applied and the people it covered. A new hire's orientation leaves the
version of each policy picked for their location and each acknowledgment
the new hire made under their own sign-in, with anything missing chased
and left open with a named owner. A concern, a disciplinary matter and a
question each leave the policy, the variant and the clause at the
version in force for the employee's location on the date, with when the
employee acknowledged it. Each approved answer is stored with its owner
and its review date beside the policy version it rests on. Nothing in
the record shows this agent deciding a policy, filling a blank a local
rule decides, or acknowledging on anyone's behalf.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
