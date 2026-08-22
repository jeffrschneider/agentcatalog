---
name: build-a-list-from-a-rule
description: The agent runs a selection rule and its exclusions against the contact database and produces the list, pool or segment it describes, with the counts checked before anything is used. Use it when running `ref/mkt/account-based-play` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: audience-operator
  agent-version: "1"
---

# Build a list from a rule

## What it does

The agent runs a selection rule and its exclusions against the contact
database and produces the list, pool or segment it describes, with the
counts checked before anything is used.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Build the Audience Pools**
  - `ref/mkt/display-retargeting`, activity 7 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Build the Contact Set**
  - `ref/mkt/account-based-play`, activity 5 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Build the List**
  - `ref/mkt/target-audience-segment`, activity 8 -
    [Build Target Audience Segment](../../../../processes/marketing/target-audience-segment.md)
- **Build the Notice Lists**
  - `ref/mkt/pricing-change`, activity 9 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)
- **Rebuild the Segments**
  - `ref/mkt/contact-database-hygiene`, activity 14 -
    [Cleanse Contact Database](../../../../processes/marketing/contact-database-hygiene.md)

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
