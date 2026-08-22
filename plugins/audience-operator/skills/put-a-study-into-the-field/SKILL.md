---
name: put-a-study-into-the-field
description: The agent sends the invitation or the ask to the sample it was given and collects what comes back, keeping track of who was approached and who answered. Use it when running `ref/mkt/brand-health` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: audience-operator
  agent-version: "1"
---

# Put a study into the field

## What it does

The agent sends the invitation or the ask to the sample it was given and
collects what comes back, keeping track of who was approached and who
answered.

## Where it happens

The agent does this in three activities across four reference processes.
Each one names the activity as that process words it.

- **Field the Study**
  - `ref/mkt/buyer-persona`, activity 7 -
    [Develop Buyer Persona](../../../../processes/marketing/buyer-persona.md)
  - `ref/mkt/customer-research`, activity 13 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
- **Field the Wave**
  - `ref/mkt/brand-health`, activity 13 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
- **Invite the Buyers**
  - `ref/mkt/win-loss-analysis`, activity 11 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)

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
