---
name: turn-claims-into-checks
description: Names the claims that decide the answer, collects what the candidate says about each one, and turns every claim into a check that can come back proven, unproven or false. Use it when running `ref/prt/qualify-a-partner`.
license: CC-BY-4.0
metadata:
  agent: partner-qualifier
  agent-version: "1"
---

# Turn claims into checks

## What it does

Names the claims that decide the answer, collects what the candidate
says about each one, and turns every claim into a check that can come
back proven, unproven or false.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Collect What the Candidate Claims**
  - `ref/prt/qualify-a-partner`, activity 3 -
    [Qualify a Partner](../../../../processes/partners/qualify-a-partner.md)
- **Set What Must Be Proven**
  - `ref/prt/qualify-a-partner`, activity 2 -
    [Qualify a Partner](../../../../processes/partners/qualify-a-partner.md)
- **Turn the Claims into Checks**
  - `ref/prt/qualify-a-partner`, activity 4 -
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
