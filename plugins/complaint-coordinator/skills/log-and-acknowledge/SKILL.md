---
name: log-and-acknowledge
description: Takes in each complaint once in the customer's own words, reads it against the complaints policy, logs it on the register with the deadline the local rule sets, and acknowledges it in the approved words. Use it when running `ref/sup/answer-a-formal-complaint`.
license: CC-BY-4.0
metadata:
  agent: complaint-coordinator
  agent-version: "1"
---

# Log and acknowledge

## What it does

Takes in each complaint once in the customer's own words, reads it
against the complaints policy, logs it on the register with the deadline
the local rule sets, and acknowledges it in the approved words.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Acknowledge the Complaint**
  - `ref/sup/answer-a-formal-complaint`, activity 5 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)
- **Check It against the Complaints Policy**
  - `ref/sup/answer-a-formal-complaint`, activity 2 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)
- **Log the Complaint with Its Deadline**
  - `ref/sup/answer-a-formal-complaint`, activity 3 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)
- **Take In the Complaint**
  - `ref/sup/answer-a-formal-complaint`, activity 1 -
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
