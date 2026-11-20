---
name: watch-for-a-surge
description: Reads what is arriving on each channel, counts the requests by symptom, sends a symptom that passes the threshold to the outage process, gathers and joins every case that describes it, and returns the cases to their queues when the engineer rules it out. Use it when running `ref/sup/raise-a-suspected-outage` and `ref/sup/run-the-days-queue`.
license: CC-BY-4.0
metadata:
  agent: request-sorter
  agent-version: "1"
---

# Watch for a surge

## What it does

Reads what is arriving on each channel, counts the requests by symptom,
sends a symptom that passes the threshold to the outage process, gathers
and joins every case that describes it, and returns the cases to their
queues when the engineer rules it out.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Gather the Cases on the Symptom**
  - `ref/sup/raise-a-suspected-outage`, activity 6 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Hold New Requests on the Symptom**
  - `ref/sup/raise-a-suspected-outage`, activity 11 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Notice a Rise on One Symptom**
  - `ref/sup/raise-a-suspected-outage`, activity 1 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)
- **Raise a Surge on One Symptom**
  - `ref/sup/run-the-days-queue`, activity 6 -
    [Run the Day's Queue](../../../../processes/customer-support/run-the-days-queue.md)
- **Read What Is Arriving**
  - `ref/sup/run-the-days-queue`, activity 5 -
    [Run the Day's Queue](../../../../processes/customer-support/run-the-days-queue.md)
- **Send Back a Ruled-Out Alarm**
  - `ref/sup/raise-a-suspected-outage`, activity 14 -
    [Raise a Suspected Outage](../../../../processes/customer-support/raise-a-suspected-outage.md)

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
