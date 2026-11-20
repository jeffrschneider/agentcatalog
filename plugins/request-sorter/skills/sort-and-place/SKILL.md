---
name: sort-and-place
description: Sorts each request by urgency and topic under the routing rules at their version, sets the service level the customer's plan carries, marks what needs a person or an identity check, places the case in its queue, and sorts again a case a specialist says is in the wrong queue. Use it when running `ref/sup/take-in-a-request`.
license: CC-BY-4.0
metadata:
  agent: request-sorter
  agent-version: "1"
---

# Sort and place

## What it does

Sorts each request by urgency and topic under the routing rules at their
version, sets the service level the customer's plan carries, marks what
needs a person or an identity check, places the case in its queue, and
sorts again a case a specialist says is in the wrong queue.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Mark What Needs a Person or a Check**
  - `ref/sup/take-in-a-request`, activity 10 -
    [Take In a Request](../../../../processes/customer-support/take-in-a-request.md)
- **Move a Misrouted Case**
  - `ref/sup/take-in-a-request`, activity 12 -
    [Take In a Request](../../../../processes/customer-support/take-in-a-request.md)
- **Place the Case in Its Queue**
  - `ref/sup/take-in-a-request`, activity 11 -
    [Take In a Request](../../../../processes/customer-support/take-in-a-request.md)
- **Set the Service Level**
  - `ref/sup/take-in-a-request`, activity 9 -
    [Take In a Request](../../../../processes/customer-support/take-in-a-request.md)
- **Sort by Urgency and Topic**
  - `ref/sup/take-in-a-request`, activity 8 -
    [Take In a Request](../../../../processes/customer-support/take-in-a-request.md)

## What to record

Each request leaves what it was as it arrived, with its channel, its
time and the customer's own words, the account it was matched to with
the details the match rested on or the mark that it matched none, the
case it opened or joined, what it was read against for anything that
cannot wait with the owner told and when, its urgency and topic with the
rule and the version behind each, its service level with the clock
running from its arrival, the marks for a person or an identity check,
and the queue it was placed in, with each move and the specialist's
reason. Each after-hours period leaves each page with its time and who
answered it, each case held with its clock, the order the held cases
were set in, and the hand-over to the morning team. Each surge leaves
the count by symptom, the time the first request arrived and every
request joined to the suspected outage, and each ruled-out alarm the
cases returned to their queues with the engineer's reason. Each routing
change leaves the replay on past requests with every request that would
land elsewhere, and the first live requests checked against the rule.
Nothing in the record shows this agent sending a reply to a customer,
reading out or changing anything in an account, deciding an urgent case
or changing a routing rule.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
