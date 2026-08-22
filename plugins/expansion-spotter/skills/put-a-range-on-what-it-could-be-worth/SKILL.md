---
name: put-a-range-on-what-it-could-be-worth
description: Writes a range with the assumptions next to it, marked as not a forecast. Use it when running `ref/sls/spot-an-expansion`.
license: CC-BY-4.0
metadata:
  agent: expansion-spotter
  agent-version: "1"
---

# Put a range on what it could be worth

## What it does

Writes a range with the assumptions next to it, marked as not a
forecast. Nothing enters a forecast at this stage.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Size What It Could Be Worth**
  - `ref/sls/spot-an-expansion`, activity 9 -
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
