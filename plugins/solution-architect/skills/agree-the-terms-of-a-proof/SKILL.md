---
name: agree-the-terms-of-a-proof
description: Decides whether the buyer needs to see the thing work on their own data. Use it when running `ref/sls/run-a-proof-of-value` and `ref/sls/shape-the-solution`.
license: CC-BY-4.0
metadata:
  agent: solution-architect
  agent-version: "1"
---

# Agree the terms of a proof

## What it does

Decides whether the buyer needs to see the thing work on their own data.
If they do, the terms are settled in writing before anything is built:
what counts as a pass, who does what on each side, and which data and
which access the proof runs on.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Agree the Data and the Access**
  - `ref/sls/run-a-proof-of-value`, activity 5 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)
- **Agree the Success Criteria**
  - `ref/sls/run-a-proof-of-value`, activity 2 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)
- **Decide Whether a Proof Is Needed**
  - `ref/sls/shape-the-solution`, activity 13 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Decide a Proof Is Warranted**
  - `ref/sls/run-a-proof-of-value`, activity 1 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)
- **Name Who Does What**
  - `ref/sls/run-a-proof-of-value`, activity 4 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)

## What to record

The shape at a version, with what the prior shapes for similar problems
taught. The separation of what ships now from what is committed and what
is only planned, with the source of each line. Every specialist reading:
who read it, what they said, and when. The build gap written as work
rather than as a promise. The cut, naming what came out and who signed
it. The requirement map, with a reason attached to every refusal, seen
by the buyer before they see the shape. The buyer's corrections in the
buyer's words. Every change after agreement raising the version and
going to everyone holding the old one. For a proof: the pass criteria
agreed in writing before anything was built, the two dates, the named
people on both sides, the line-by-line score with its evidence, and what
the result corrected in the shape.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
