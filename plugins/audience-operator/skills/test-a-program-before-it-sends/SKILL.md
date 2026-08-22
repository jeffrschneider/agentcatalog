---
name: test-a-program-before-it-sends
description: With sending switched off, the agent walks test contacts down every branch of a program and records what each one did. Use it when running `ref/mkt/nurture-sequence`.
license: CC-BY-4.0
metadata:
  agent: audience-operator
  agent-version: "1"
---

# Test a program before it sends

## What it does

With sending switched off, the agent walks test contacts down every
branch of a program and records what each one did.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Run Test Contacts Through It**
  - `ref/mkt/nurture-sequence`, activity 12 -
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
