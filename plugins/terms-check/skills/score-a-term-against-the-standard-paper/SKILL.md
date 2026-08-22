---
name: score-a-term-against-the-standard-paper
description: Takes a proposed term, names the clause of the standard it departs from at the version in force, and states the direction and the size of the departure rather than passing or failing the document as a whole. Use it when running `ref/rev/review-a-non-standard-deal`.
license: CC-BY-4.0
metadata:
  agent: terms-check
  agent-version: "1"
---

# Score a term against the standard paper

## What it does

Takes a proposed term, names the clause of the standard it departs from
at the version in force, and states the direction and the size of the
departure rather than passing or failing the document as a whole. A term
the standard has no clause for is recorded as unscorable with the
reason, never as passed.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Test the Terms Against the Standard**
  - `ref/rev/review-a-non-standard-deal`, activity 6 -
    [Review a Non-Standard Deal](../../../../processes/revenue-operations/review-a-non-standard-deal.md)

## What to record

Per term: the clause of the standard it was scored against, the version
that clause was read at, whether it departs, in which direction, and how
far. Every term the standard has no clause for is recorded as unscorable
with the reason, never as passed. When it scores a draft approval table,
each band carries a pass or the rule behind its failure. Every score
names the item in the words it was given, so somebody auditing a run can
read the same clause at the same version and get the same answer without
asking this agent what it meant.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
