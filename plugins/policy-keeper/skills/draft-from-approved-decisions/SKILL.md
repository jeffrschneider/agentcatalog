---
name: draft-from-approved-decisions
description: Drafts a change on the current version only from an approved decision, a rule change counsel confirmed or an audit finding, and writes a location's variant only where a local rule needs a different text, with every local point left blank for counsel. Use it when running `ref/hr/issue-a-disciplinary-action`, `ref/hr/publish-an-hr-policy` and `ref/hr/resolve-an-employee-concern`.
license: CC-BY-4.0
metadata:
  agent: policy-keeper
  agent-version: "1"
---

# Draft from approved decisions

## What it does

Drafts a change on the current version only from an approved decision, a
rule change counsel confirmed or an audit finding, and writes a
location's variant only where a local rule needs a different text, with
every local point left blank for counsel. It drafts the changes a case
shows are needed once a named person has decided them.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Act on the Outcome**
  - `ref/hr/resolve-an-employee-concern`, activity 14 -
    [Resolve an Employee Concern](../../../../processes/human-resources/resolve-an-employee-concern.md)
- **Draft the Change**
  - `ref/hr/publish-an-hr-policy`, activity 4 -
    [Publish an HR Policy](../../../../processes/human-resources/publish-an-hr-policy.md)
- **Record What the Case Taught**
  - `ref/hr/issue-a-disciplinary-action`, activity 18 -
    [Issue a Disciplinary Action](../../../../processes/human-resources/issue-a-disciplinary-action.md)
- **Write the Location Variants**
  - `ref/hr/publish-an-hr-policy`, activity 5 -
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
