---
name: program-operation
description: Runs a program after it goes live, which means switching it on when the owner says go, reading who enters, which path they take, who converts and who leaves, and changing the steps and rules the numbers argue against. Use it when running `ref/mkt/nurture-sequence`.
license: CC-BY-4.0
metadata:
  agent: audience-manager
  agent-version: "1"
---

# Program operation

## What it does

Runs a program after it goes live, which means switching it on when the
owner says go, reading who enters, which path they take, who converts
and who leaves, and changing the steps and rules the numbers argue
against.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Tune the Branches**
  - `ref/mkt/nurture-sequence`, activity 16 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Turn It On**
  - `ref/mkt/nurture-sequence`, activity 13 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- **Watch Who Moves**
  - `ref/mkt/nurture-sequence`, activity 14 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)

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
