---
name: check-the-suppression-is-holding
description: No impressions went to anyone the list took out. Use it when running `ref/mkt/display-retargeting`.
license: CC-BY-4.0
metadata:
  agent: audience-operator
  agent-version: "1"
---

# Check the Suppression Is Holding

## What happens

No impressions went to anyone the list took out.

## Where it happens

- `ref/mkt/display-retargeting`, activity 15 -
  [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)

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
