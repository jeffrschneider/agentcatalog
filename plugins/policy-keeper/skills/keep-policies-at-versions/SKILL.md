---
name: keep-policies-at-versions
description: Takes in each request with the decision behind it, reads the current version and who each variant covers, publishes each variant at its version with its effective date, and keeps the old version with the dates it applied. Use it when running `ref/hr/publish-an-hr-policy`.
license: CC-BY-4.0
metadata:
  agent: policy-keeper
  agent-version: "1"
---

# Keep policies at versions

## What it does

Takes in each request with the decision behind it, reads the current
version and who each variant covers, publishes each variant at its
version with its effective date, and keeps the old version with the
dates it applied. It marks every answer, form and page that rests on the
old version and records the publication.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Keep the Old Version With Its Dates**
  - `ref/hr/publish-an-hr-policy`, activity 14 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Mark What Rests on the Old Version**
  - `ref/hr/publish-an-hr-policy`, activity 13 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Publish the Policy at a Version**
  - `ref/hr/publish-an-hr-policy`, activity 9 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Read the Current Version**
  - `ref/hr/publish-an-hr-policy`, activity 2 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Record the Publication**
  - `ref/hr/publish-an-hr-policy`, activity 15 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Take in the Policy Request**
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
