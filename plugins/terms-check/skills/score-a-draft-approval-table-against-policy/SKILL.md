---
name: score-a-draft-approval-table-against-policy
description: Reads a draft set of approval levels against the delegation of authority, the standard paper and whatever a signature has to satisfy. Use it when running `ref/rev/publish-the-approval-thresholds`.
license: CC-BY-4.0
metadata:
  agent: terms-check
  agent-version: "1"
---

# Score a draft approval table against policy

## What it does

Reads a draft set of approval levels against the delegation of
authority, the standard paper and whatever a signature has to satisfy.
Each band comes back with a pass or the rule behind its failure.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check the Levels Against Policy**
  - `ref/rev/publish-the-approval-thresholds`, activity 7 -
    [Publish the Approval Thresholds](../../../../processes/revenue-operations/publish-the-approval-thresholds.md)

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
