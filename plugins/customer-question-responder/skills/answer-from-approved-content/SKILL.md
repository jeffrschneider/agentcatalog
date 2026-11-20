---
name: answer-from-approved-content
description: Writes each answer from approved content and the customer's own records alone, checks every sentence against them, sends it as an agent with the article named and a way to reach a person, by day, after hours or from the latest approved update, and asks whether it settled the question. Use it when running `ref/sup/answer-a-billing-question` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: customer-question-responder
  agent-version: "1"
---

# Answer from approved content

## What it does

Writes each answer from approved content and the customer's own records
alone, checks every sentence against them, sends it as an agent with the
article named and a way to reach a person, by day, after hours or from
the latest approved update, and asks whether it settled the question.

## Where it happens

The agent does this in eight activities across five reference processes.
Each one names the activity as that process words it.

- **Answer What Approved Content Covers**
  - `ref/sup/cover-after-hours-requests`, activity 8 -
    [Cover After-Hours Requests](../../../../processes/customer-support/cover-after-hours-requests.md)
- **Answer a New Case from the Approved Update**
  - `ref/sup/tell-affected-customers`, activity 10 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Answer from Approved Content**
  - `ref/sup/answer-a-billing-question`, activity 6 -
    [Answer a Billing Question](../../../../processes/customer-support/answer-a-billing-question.md)
- **Answer the Replies**
  - `ref/sup/tell-customers-about-a-fix`, activity 8 -
    [Tell Customers about a Fix](../../../../processes/customer-support/tell-customers-about-a-fix.md)
- **Check the Answer Before It Goes**
  - `ref/sup/answer-a-routine-question`, activity 8 -
    [Answer a Routine Question](../../../../processes/customer-support/answer-a-routine-question.md)
- **Check the Question Is Settled**
  - `ref/sup/answer-a-routine-question`, activity 12 -
    [Answer a Routine Question](../../../../processes/customer-support/answer-a-routine-question.md)
- **Send the Answer as an Agent**
  - `ref/sup/answer-a-routine-question`, activity 9 -
    [Answer a Routine Question](../../../../processes/customer-support/answer-a-routine-question.md)
- **Write the Answer from Approved Content**
  - `ref/sup/answer-a-routine-question`, activity 7 -
    [Answer a Routine Question](../../../../processes/customer-support/answer-a-routine-question.md)

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
