---
name: hand-the-queue-between-shifts
description: Holds each case that waits for a person overnight with its clock running, sets the held cases in order of urgency and service level, hands them to the morning team, and hands the cases still waiting at the close to the person on call. Use it when running `ref/sup/cover-after-hours-requests` and `ref/sup/run-the-days-queue`.
license: CC-BY-4.0
metadata:
  agent: request-sorter
  agent-version: "1"
---

# Hand the queue between shifts

## What it does

Holds each case that waits for a person overnight with its clock
running, sets the held cases in order of urgency and service level,
hands them to the morning team, and hands the cases still waiting at the
close to the person on call.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Hand Over to the Morning Team**
  - `ref/sup/cover-after-hours-requests`, activity 13 -
    [Cover After-Hours Requests](../../../../processes/customer-support/cover-after-hours-requests.md)
- **Hand the Queue to After-Hours Cover**
  - `ref/sup/run-the-days-queue`, activity 14 -
    [Run the Day's Queue](../../../../processes/customer-support/run-the-days-queue.md)
- **Hold What Waits for Morning**
  - `ref/sup/cover-after-hours-requests`, activity 10 -
    [Cover After-Hours Requests](../../../../processes/customer-support/cover-after-hours-requests.md)
- **Set the Held Cases in Order**
  - `ref/sup/cover-after-hours-requests`, activity 11 -
    [Cover After-Hours Requests](../../../../processes/customer-support/cover-after-hours-requests.md)
- **Take Over the Overnight Cases**
  - `ref/sup/run-the-days-queue`, activity 2 -
    [Run the Day's Queue](../../../../processes/customer-support/run-the-days-queue.md)

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
