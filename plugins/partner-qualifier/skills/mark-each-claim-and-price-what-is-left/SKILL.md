---
name: mark-each-claim-and-price-what-is-left
description: Sets every claim against what the checks found and marks it proven, unproven or false, then prices what the claims still unproven would cost if they turned out to be wrong. Use it when running `ref/prt/qualify-a-partner`.
license: CC-BY-4.0
metadata:
  agent: partner-qualifier
  agent-version: "1"
---

# Mark each claim and price what is left

## What it does

Sets every claim against what the checks found and marks it proven,
unproven or false, then prices what the claims still unproven would cost
if they turned out to be wrong.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Price the Risk That Is Left**
  - `ref/prt/qualify-a-partner`, activity 14 -
    [Qualify a Partner](../../../../processes/partners/qualify-a-partner.md)
- **Set Claim Against Finding**
  - `ref/prt/qualify-a-partner`, activity 13 -
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
