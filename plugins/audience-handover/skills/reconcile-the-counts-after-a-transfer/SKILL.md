---
name: reconcile-the-counts-after-a-transfer
description: The agent sets what it sent against what the receiving system recorded, reports how much of the list matched at the other end, and matches both sides' counts and costs into one set of figures. Use it when running `ref/mkt/co-marketing-campaign` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: audience-handover
  agent-version: "1"
---

# Reconcile the counts after a transfer

## What it does

The agent sets what it sent against what the receiving system recorded,
reports how much of the list matched at the other end, and matches both
sides' counts and costs into one set of figures.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Agree the Joint Numbers**
  - `ref/mkt/co-marketing-campaign`, activity 15 -
    [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)
- **Confirm the Match**
  - `ref/mkt/target-audience-segment`, activity 14 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)

## What to record

For every transfer: the list at the version it was approved at, the
count it started with, the count the consent record took out, the fields
that were sent, and the fields that were held back with the term that
held each one back. The date and time the transfer went, the count the
receiving system accepted, the count it rejected with the reason it
gave, and how much of the list matched. The approval the transfer rests
on, naming the person who signed for it. The date the receiving
organization is required to delete the records, taken from the
agreement. A dated line for every withdrawal passed on after the
transfer, naming the system it went to and the day that system confirmed
it. A transfer whose receipt never arrived is recorded as unconfirmed
rather than left out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
