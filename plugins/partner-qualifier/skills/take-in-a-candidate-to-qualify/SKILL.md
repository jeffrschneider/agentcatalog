---
name: take-in-a-candidate-to-qualify
description: Takes the confirmed short list and its scores from the search that produced it, and opens a run against one candidate and the gap that candidate is meant to close. Use it when running `ref/prt/find-a-partner` and `ref/prt/qualify-a-partner`.
license: CC-BY-4.0
metadata:
  agent: partner-qualifier
  agent-version: "1"
---

# Take in a candidate to qualify

## What it does

Takes the confirmed short list and its scores from the search that
produced it, and opens a run against one candidate and the gap that
candidate is meant to close.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Hand the Short List On**
  - `ref/prt/find-a-partner`, activity 16 -
    [Find a Partner](../../../../processes/partners/find-a-partner.md)
- **Take in the Candidate and the Gap**
  - `ref/prt/qualify-a-partner`, activity 1 -
    [Qualify a Partner](../../../../processes/partners/qualify-a-partner.md)

## What to record

The claim register at a version: every claim that decides the answer,
marked proven, unproven or false, naming what settled it, where that
came from and the date it was read. The reference notes with the
question set they were taken against, and which references we found
rather than were offered. The real-work record, naming the data it ran
on and who cleared that data. The residual risk with the assumption
behind each number. Anyone auditing the run can recompute the
recommendation from what is on the record, or say which claim they would
mark differently.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
