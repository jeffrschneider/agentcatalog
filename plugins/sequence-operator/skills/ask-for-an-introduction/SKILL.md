---
name: ask-for-an-introduction
description: Writes the note an introducer can send as it stands, gets it to them with a date, and sends one reminder before the referral is let go. Use it when running `ref/sls/work-a-referral`.
license: CC-BY-4.0
metadata:
  agent: sequence-operator
  agent-version: "1"
---

# Ask for an introduction

## What it does

Writes the note an introducer can send as it stands, gets it to them
with a date, and sends one reminder before the referral is let go.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Ask for the Introduction**
  - `ref/sls/work-a-referral`, activity 9 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)
- **Wait and Chase Once**
  - `ref/sls/work-a-referral`, activity 10 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)
- **Write the Introduction**
  - `ref/sls/work-a-referral`, activity 8 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)

## What to record

The cadence and the wording as signed, at a version, with the signer and
the date, and any change after signing recorded as voiding that
signature. Per person: every touch sent, on which channel and on which
day, what the call notes say, the reply as it arrived and how it was
sorted into wants a conversation, not now, wrong person or stop, the
time the stop took effect, and the words behind any opt-out. Per run:
the bounces, complaints and blocks read against the sending thresholds,
every send held back and why, the people who reached the end of the
cadence without answering, and the touches cancelled when the sequence
closed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
