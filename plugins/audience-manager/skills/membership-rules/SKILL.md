---
name: membership-rules
description: Writes the rule that decides whether a record belongs, which covers the conditions a record has to meet, how long it stays in once it qualifies, who is deliberately kept out, and which groups must never overlap. Use it when running `ref/mkt/display-retargeting` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: audience-manager
  agent-version: "1"
---

# Membership rules

## What it does

Writes the rule that decides whether a record belongs, which covers the
conditions a record has to meet, how long it stays in once it qualifies,
who is deliberately kept out, and which groups must never overlap.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Define the Retargeting Pools**
  - `ref/mkt/display-retargeting`, activity 4 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Name the Exclusions**
  - `ref/mkt/target-audience-segment`, activity 5 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Write the Membership Rule**
  - `ref/mkt/target-audience-segment`, activity 4 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)

## What to record

Each program at a version, naming the entry condition, every step, every
wait, the condition on every branch, and every exit. The hygiene cycle's
scope at a version, saying which records it covers and what it has to
fix in them. The rule that settles which program takes a contact who
qualifies for two, with the date it was decided and who decided it. A
dated account of the database between cycles: how many records there
are, how many are complete enough to use, and how many may be contacted.
The CONVENED and DONE records of everything it convenes. The go record
for a program, naming the version that started sending and who said go.
The standing readout at the cadence the process sets, and the decision
it made after reading it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
