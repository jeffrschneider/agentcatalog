---
name: answer-from-the-library
description: Reads only the facts that decide which answer applies, matches an approved answer that rests on the policy version in force, reads it back against the policy, and answers with the source and its version inside the promised time. Use it when running `ref/hr/answer-an-employees-question`.
license: CC-BY-4.0
metadata:
  agent: employee-question-responder
  agent-version: "1"
---

# Answer from the library

## What it does

Reads only the facts that decide which answer applies, matches an
approved answer that rests on the policy version in force, reads it back
against the policy, and answers with the source and its version inside
the promised time. It asks whether the answer settled the question and
closes the question on the record.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Answer the Employee**
  - `ref/hr/answer-an-employees-question`, activity 10 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Check the Question Is Settled**
  - `ref/hr/answer-an-employees-question`, activity 14 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Close the Question on the Record**
  - `ref/hr/answer-an-employees-question`, activity 15 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Match an Approved Answer**
  - `ref/hr/answer-an-employees-question`, activity 8 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Read Only What Decides the Answer**
  - `ref/hr/answer-an-employees-question`, activity 6 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Read the Answer Against the Policy**
  - `ref/hr/answer-an-employees-question`, activity 9 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)

## What to record

Each question leaves what was asked, the channel it came through, the
time it arrived and the answer time set for it, the match of the asker
to one employee record, and the reading of whether it is personal or
sensitive. An answered question leaves the facts read to choose the
answer, the approved answer with its source and its version, the check
against the policy text, the time it was sent, and whether the employee
said it settled the question. A passed question leaves only its subject,
the reason it was passed and the named person who took it. A records
request leaves the request as recognized, the acknowledgment with its
deadline in the approved text, and each question about the answer
answered from the approved text or passed to the privacy lead. Nothing
in the record shows this agent approving, refusing or promising leave, a
pay change, an accommodation or any other decision about a person.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
