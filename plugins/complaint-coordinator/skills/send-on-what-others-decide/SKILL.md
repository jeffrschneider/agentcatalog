---
name: send-on-what-others-decide
description: Sends a legal threat or a regulator's letter to the legal team the same day, and any refund or credit an answer would offer to the process where a named person decides it. Use it when running `ref/sup/answer-a-formal-complaint`.
license: CC-BY-4.0
metadata:
  agent: complaint-coordinator
  agent-version: "1"
---

# Send on what others decide

## What it does

Sends a legal threat or a regulator's letter to the legal team the same
day, and any refund or credit an answer would offer to the process where
a named person decides it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Get Any Refund or Credit Decided**
  - `ref/sup/answer-a-formal-complaint`, activity 11 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)
- **Send Anything Legal the Same Day**
  - `ref/sup/answer-a-formal-complaint`, activity 4 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)

## What to record

Each complaint leaves its words as the customer gave them, the channel,
the date, the account and the cases, the reading against the complaints
policy with any doubt and the complaints lead's decision on it, the
register entry with its class and its deadline, anything sent to the
legal team and when, the acknowledgment as sent, the records gathered
with where each was read, any refund or credit sent to its process with
the named person's decision, any review with who held it and what it
decided, the outcome of each point with the dates and the route further,
and the cause sent to its owner. The register keeps each complaint for
the period `<your jurisdiction's rule on keeping complaint records>`
sets, ready for any report `<your jurisdiction's rules on complaints>`
require. Nothing in the record shows this agent deciding a point,
writing or sending an answer, offering money, or deciding anything about
the job of a support person.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
