---
name: record-what-intake-taught
description: Records which cases were misrouted and by which rule, which senders could not be matched, which joins were undone and which urgent requests reached their owner late. Use it when running `ref/sup/take-in-a-request`.
license: CC-BY-4.0
metadata:
  agent: request-sorter
  agent-version: "1"
---

# Record what intake taught

## What it does

Records which cases were misrouted and by which rule, which senders
could not be matched, which joins were undone and which urgent requests
reached their owner late.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Record What the Intake Taught**
  - `ref/sup/take-in-a-request`, activity 13 -
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
