---
name: cut-to-a-shortlist
description: Drop the candidates that miss a requirement. Use it when running `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: supplier-check
  agent-version: "1"
---

# Cut to a Shortlist

## What happens

Drop the candidates that miss a requirement.

## Where it happens

- `ref/mkt/select-marketing-technology`, activity 9 -
  [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)

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
