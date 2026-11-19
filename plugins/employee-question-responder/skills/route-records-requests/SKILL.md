---
name: route-records-requests
description: Recognizes a records request in the help channel, acknowledges it with its deadline in the approved text, and answers questions about the answer from the approved text, passing any question about what was withheld to the privacy lead. Use it when running `ref/hr/answer-a-records-request`.
license: CC-BY-4.0
metadata:
  agent: employee-question-responder
  agent-version: "1"
---

# Route records requests

## What it does

Recognizes a records request in the help channel, acknowledges it with
its deadline in the approved text, and answers questions about the
answer from the approved text, passing any question about what was
withheld to the privacy lead.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Acknowledge the Request**
  - `ref/hr/answer-a-records-request`, activity 2 -
    [Answer a Records Request](../../../../processes/human-resources/answer-a-records-request.md)
- **Answer Questions About the Answer**
  - `ref/hr/answer-a-records-request`, activity 15 -
    [Answer a Records Request](../../../../processes/human-resources/answer-a-records-request.md)
- **Take in the Request**
  - `ref/hr/answer-a-records-request`, activity 1 -
    [Answer a Records Request](../../../../processes/human-resources/answer-a-records-request.md)

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
