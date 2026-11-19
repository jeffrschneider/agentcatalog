---
name: say-which-version-applies
description: Finds the policy, the variant and the clause in force for a person's location on a given date, with when the person acknowledged it, for a concern, a conduct matter, a question, each new hire and the orientation material. Use it when running `ref/hr/answer-an-employees-question` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: policy-keeper
  agent-version: "1"
---

# Say which version applies

## What it does

Finds the policy, the variant and the clause in force for a person's
location on a given date, with when the person acknowledged it, for a
concern, a conduct matter, a question, each new hire and the orientation
material.

## Where it happens

The agent does this in five activities across four reference processes.
Each one names the activity as that process words it.

- **Check the Material Is Current**
  - `ref/hr/run-new-hire-orientation`, activity 3 -
    [Run New Hire Orientation](../../../../processes/human-resources/run-new-hire-orientation.md)
- **Find the Policy That Applies**
  - `ref/hr/answer-an-employees-question`, activity 7 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Pick Each Location's Policies**
  - `ref/hr/run-new-hire-orientation`, activity 5 -
    [Run New Hire Orientation](../../../../processes/human-resources/run-new-hire-orientation.md)
- **Read the Policy That Applied**
  - `ref/hr/issue-a-disciplinary-action`, activity 3 -
    [Issue a Disciplinary Action](../../../../processes/human-resources/issue-a-disciplinary-action.md)
  - `ref/hr/resolve-an-employee-concern`, activity 5 -
    [Resolve an Employee Concern](../../../../processes/human-resources/resolve-an-employee-concern.md)
- **Record the Outcome**
  - `ref/hr/issue-a-disciplinary-action`, activity 13 -
    [Issue a Disciplinary Action](../../../../processes/human-resources/issue-a-disciplinary-action.md)

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
