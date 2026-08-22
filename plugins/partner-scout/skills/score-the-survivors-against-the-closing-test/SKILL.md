---
name: score-the-survivors-against-the-closing-test
description: Scores every candidate that survives screening against the test the gap set, with the evidence line behind each score and the date that evidence was read. Use it when running `ref/prt/find-a-partner`.
license: CC-BY-4.0
metadata:
  agent: partner-scout
  agent-version: "1"
---

# Score the survivors against the closing test

## What it does

Scores every candidate that survives screening against the test the gap
set, with the evidence line behind each score and the date that evidence
was read.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Score the Candidates**
  - `ref/prt/find-a-partner`, activity 10 -
    [Find a Partner](../../../../processes/partners/find-a-partner.md)

## What to record

The search bounds it was given, including the companies it may not
touch. Every candidate with the source it came from and the date it was
read. Every removal with the reason it was removed. Every score against
the closing test with the evidence line behind it and the date that
evidence was read, so a second person scoring the same candidate can get
the same answer or say where they differ. The approach as sent, the
date, and what each candidate was told. The replies, the refusals and
the silences, each dated.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
