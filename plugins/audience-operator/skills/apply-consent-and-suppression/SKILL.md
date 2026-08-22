---
name: apply-consent-and-suppression
description: Everyone the consent record does not cover comes out. Use it when running `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: audience-operator
  agent-version: "1"
---

# Apply Consent and Suppression

## What happens

Everyone the consent record does not cover comes out.

## Where it happens

- `ref/mkt/target-audience-segment`, activity 9 -
  [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)

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
