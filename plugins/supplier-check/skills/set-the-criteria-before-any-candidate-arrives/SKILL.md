---
name: set-the-criteria-before-any-candidate-arrives
description: The agent writes down how a candidate or a proposal will be judged and fixes that list at a version before the first candidate is seen. Use it when running `ref/mkt/engage-marketing-agency` and `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: supplier-check
  agent-version: "1"
---

# Set the criteria before any candidate arrives

## What it does

The agent writes down how a candidate or a proposal will be judged and
fixes that list at a version before the first candidate is seen. Every
candidate is then scored against the same list in the same order,
whenever it arrived.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Set the Scoring Criteria**
  - `ref/mkt/select-marketing-technology`, activity 4 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Set the Selection Criteria**
  - `ref/mkt/engage-marketing-agency`, activity 6 -
    [Engage Marketing Agency](../../../../processes/marketing/engage-marketing-agency.md)

## What to record

It leaves a scoring sheet for each candidate at a version, naming the
requirements list and the version it scored against, with one row per
requirement carrying the verdict and the evidence behind it. The
evidence names the demonstration step, the document, or the reference
call it came from, so a person can check a verdict without asking the
agent what it meant. A requirement it could not test is recorded as not
tested, with the reason it could not be tested. When a candidate revises
its material, the rescore says what changed, what was run again, and
what was carried over from the earlier score. It records the date each
candidate's material arrived and the date it was scored.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
