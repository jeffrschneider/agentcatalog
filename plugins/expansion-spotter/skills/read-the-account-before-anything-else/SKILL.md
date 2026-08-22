---
name: read-the-account-before-anything-else
description: Checks whether the account may be approached at all, given collections, disputes and any open support crisis, and reads what they own today with the limit on every metered line. Use it when running `ref/sls/spot-an-expansion`.
license: CC-BY-4.0
metadata:
  agent: expansion-spotter
  agent-version: "1"
---

# Read the account before anything else

## What it does

Checks whether the account may be approached at all, given collections,
disputes and any open support crisis, and reads what they own today with
the limit on every metered line. Also picks up which teams started using
what, and when.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check the Account Is Approachable**
  - `ref/sls/spot-an-expansion`, activity 2 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)
- **Look for the Teams Newly Adopting**
  - `ref/sls/spot-an-expansion`, activity 5 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)
- **Read What They Already Own**
  - `ref/sls/spot-an-expansion`, activity 3 -
    [Spot an Expansion](../../../../processes/sales/spot-an-expansion.md)

## What to record

Per signal: the account's standing, dated, with any reason it may not be
approached at all. What they own today with the limit on every metered
line. The teams that started using what, and when. The opening as one
sentence at a version, with whatever the renewal already covers and
whatever an open deal already covers taken out of it. A range with the
assumptions written next to it, marked as not a forecast. The named
people the change would land on, and what each of them said in their own
words, with the date and who heard it. What delivery said about the
account. The score with the model version, every input, and the evidence
each input came from. The decision, who made it, when, and the reason in
their words. A dropped opening keeps all of it, so the same reading does
not raise the same opening next month.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
