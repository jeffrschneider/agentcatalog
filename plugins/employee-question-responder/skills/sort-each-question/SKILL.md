---
name: sort-each-question
description: Takes in each question, matches the asker to one employee record before reading anything about a person, and reads whether the question is personal or sensitive. Use it when running `ref/hr/answer-an-employees-question`.
license: CC-BY-4.0
metadata:
  agent: employee-question-responder
  agent-version: "1"
---

# Sort each question

## What it does

Takes in each question, matches the asker to one employee record before
reading anything about a person, and reads whether the question is
personal or sensitive. It passes any that is to the named person for its
subject, with the employee told who has it.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Confirm Who Is Asking**
  - `ref/hr/answer-an-employees-question`, activity 2 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Pass It to a Named Person**
  - `ref/hr/answer-an-employees-question`, activity 4 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Spot What Is Personal or Sensitive**
  - `ref/hr/answer-an-employees-question`, activity 3 -
    [Answer an Employee's Question](../../../../processes/human-resources/answer-an-employees-question.md)
- **Take in the Question**
  - `ref/hr/answer-an-employees-question`, activity 1 -
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
