---
name: send-approved-wording
description: Sends exactly the approved wording to each linked customer, each contact an agreement names and the other affected accounts, by the route each is owed and before any deadline, and only once a customer has the change it describes. Use it when running `ref/sup/tell-affected-customers` and `ref/sup/tell-customers-about-a-fix`.
license: CC-BY-4.0
metadata:
  agent: customer-question-responder
  agent-version: "1"
---

# Send approved wording

## What it does

Sends exactly the approved wording to each linked customer, each contact
an agreement names and the other affected accounts, by the route each is
owed and before any deadline, and only once a customer has the change it
describes.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Send Each Later Update**
  - `ref/sup/tell-affected-customers`, activity 12 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Send Each Notice an Agreement Names**
  - `ref/sup/tell-affected-customers`, activity 7 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Send the Notice to Each Linked Customer**
  - `ref/sup/tell-customers-about-a-fix`, activity 7 -
    [Tell Customers about a Fix](../../../../processes/customer-support/tell-customers-about-a-fix.md)
- **Send the Resolved Update**
  - `ref/sup/tell-affected-customers`, activity 13 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)
- **Tell the Other Affected Accounts**
  - `ref/sup/tell-affected-customers`, activity 8 -
    [Tell Affected Customers](../../../../processes/customer-support/tell-affected-customers.md)

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
