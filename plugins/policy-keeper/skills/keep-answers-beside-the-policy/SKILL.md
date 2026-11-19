---
name: keep-answers-beside-the-policy
description: Reads each matched answer back against the policy text it cites, and stores each approved answer beside the policy version it rests on, with its owner and its review date. Use it when running `ref/hr/answer-an-employees-question`.
license: CC-BY-4.0
metadata:
  agent: policy-keeper
  agent-version: "1"
---

# Keep answers beside the policy

## What it does

Reads each matched answer back against the policy text it cites, and
stores each approved answer beside the policy version it rests on, with
its owner and its review date.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Add the Answer to the Library**
  - `ref/hr/answer-an-employees-question`, activity 13 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Read the Answer Against the Policy**
  - `ref/hr/answer-an-employees-question`, activity 9 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)

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
