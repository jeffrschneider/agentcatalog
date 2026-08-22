---
name: built-thing-verification
description: Takes a sample of what was built and puts it back through the rule it came from, whether that is a set of records read back against the membership rule or a test contact walked down every path of a program, and reports where the two disagree. Use it when running `ref/mkt/nurture-sequence` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: audience-manager
  agent-version: "1"
---

# Built thing verification

## What it does

Takes a sample of what was built and puts it back through the rule it
came from, whether that is a set of records read back against the
membership rule or a test contact walked down every path of a program,
and reports where the two disagree.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Built List**
  - `ref/mkt/target-audience-segment`, activity 10 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Run Test Contacts Through It**
  - `ref/mkt/nurture-sequence`, activity 12 -
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
