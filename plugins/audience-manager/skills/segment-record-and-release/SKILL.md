---
name: segment-record-and-release
description: Writes the finished segment down with its definition, its counts and where it goes, sets how often it is rebuilt and delivered again and when it gets looked at again, and puts a list that will leave the organization in front of a person to approve first. Use it when running `ref/mkt/buyer-persona` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: audience-manager
  agent-version: "1"
---

# Segment record and release

## What it does

Writes the finished segment down with its definition, its counts and
where it goes, sets how often it is rebuilt and delivered again and when
it gets looked at again, and puts a list that will leave the
organization in front of a person to approve first.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Approve the Release**
  - `ref/mkt/target-audience-segment`, activity 12 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Record the Segment**
  - `ref/mkt/target-audience-segment`, activity 16 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Set the Refresh Schedule**
  - `ref/mkt/target-audience-segment`, activity 15 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Set the Review Conditions**
  - `ref/mkt/buyer-persona`, activity 19 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)

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
