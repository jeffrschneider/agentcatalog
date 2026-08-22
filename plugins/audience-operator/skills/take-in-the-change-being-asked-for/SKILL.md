---
name: take-in-the-change-being-asked-for
description: The agent sits in the briefing that starts a change and takes down what is being asked for, what it is for, and which design or plan it builds to. Use it when running `ref/mkt/contact-database-hygiene`, `ref/mkt/nurture-sequence` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: audience-operator
  agent-version: "1"
---

# Take in the change being asked for

## What it does

The agent sits in the briefing that starts a change and takes down what
is being asked for, what it is for, and which design or plan it builds
to.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Brief the Build**
  - `ref/mkt/target-audience-segment`, activity 7 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Brief the Cycle**
  - `ref/mkt/contact-database-hygiene`, activity 4 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
- **Brief the Makers**
  - `ref/mkt/nurture-sequence`, activity 6 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)

## What to record

For every change, the counts before and after it, field by field, and
where the copy that puts the change back is kept. For every merge, which
records went into which, what was kept from each, and what was dropped.
For every filled field, the source it came from and the date it was
read. For every removal, what came out and the person who signed for it.
The program as it was built, at a version, with every step, wait,
condition and exit set beside the design it was built from, and a test
record showing a contact going down each branch. Anything it could not
build as designed is recorded as unbuilt rather than left out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
