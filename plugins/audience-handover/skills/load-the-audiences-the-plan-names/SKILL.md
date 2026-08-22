---
name: load-the-audiences-the-plan-names
description: The audiences reach the platforms with consent applied. Use it when running `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: audience-handover
  agent-version: "1"
---

# Load the Audiences the Plan Names

## What happens

The audiences reach the platforms with consent applied.

## Where it happens

- `ref/mkt/traffic-ad-creative`, activity 11 -
  [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

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
