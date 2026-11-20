---
name: hand-to-a-person
description: Passes a case a person must take to a support specialist with a draft, what was found and why, and tells the customer in the approved words when a person will reply. Use it when running `ref/sup/answer-a-billing-question` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: customer-question-responder
  agent-version: "1"
---

# Hand to a person

## What it does

Passes a case a person must take to a support specialist with a draft,
what was found and why, and tells the customer in the approved words
when a person will reply.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Hand the Case to a Person**
  - `ref/sup/answer-a-routine-question`, activity 11 -
    [Answer a Routine Question](../../../../processes/customer-support/answer-a-routine-question.md)
- **Pass What the Update Does Not Answer**
  - `ref/sup/tell-affected-customers`, activity 11 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Pass the Question to a Specialist**
  - `ref/sup/answer-a-billing-question`, activity 7 -
    [Answer a Billing Question](../../../../processes/customer-support/answer-a-billing-question.md)
- **Tell Each Other Customer When a Person Will Reply**
  - `ref/sup/cover-after-hours-requests`, activity 9 -
    [Cover After-Hours Requests](../../../../processes/customer-support/cover-after-hours-requests.md)

## What to record

Each answer leaves the question as it arrived, the category it was read
under, the content and its version, the parts of the record read with
where each was read, each sentence traced to the content or the record
it rests on, the reply as sent with the article it named and its words
saying it comes from an agent and how to reach a person, the time it
took against the service level, and whether the customer said it settled
the question. Each case handed to a person leaves what was found, the
draft, the reason it needs a person and the words the customer was sent.
Each billing question leaves how the message was sorted, the invoice,
charge or payment read, and the article the answer rested on. Each
notice about an incident leaves the approved version sent, the case or
contact it went to, the route, and the time against any deadline an
agreement names. Each notice about a fix leaves its version and the team
lead's approval, each customer it went to and when, each reply and how
it was answered. Nothing in the record shows this agent answering from
general knowledge, sending words a named person had not approved,
sending a reply in a category kept for a person, promising a fix, a date
or money, or changing anything in an account or a bill.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
