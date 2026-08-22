---
name: apply-consent-and-suppression
description: The agent takes out everyone the consent record does not cover and everyone on a suppression list, and writes that exclusion into every list and system the change touches. Use it when running `ref/mkt/contact-database-hygiene`, `ref/mkt/display-retargeting` and `ref/mkt/target-audience-segment`.
license: CC-BY-4.0
metadata:
  agent: audience-operator
  agent-version: "1"
---

# Apply consent and suppression

## What it does

The agent takes out everyone the consent record does not cover and
everyone on a suppression list, and writes that exclusion into every
list and system the change touches.

## Where it happens

The agent does this in two activities across three reference processes.
Each one names the activity as that process words it.

- **Apply Consent and Suppression**
  - `ref/mkt/target-audience-segment`, activity 9 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Apply the Suppression**
  - `ref/mkt/contact-database-hygiene`, activity 13 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)
  - `ref/mkt/display-retargeting`, activity 8 -
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
