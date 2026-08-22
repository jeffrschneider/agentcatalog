---
name: record-what-the-run-taught
description: "Files what a shaping run or a proof taught: what the result corrected in the shape, and what to do differently the next time the same problem comes round. Use it when running `ref/sls/run-a-proof-of-value` and `ref/sls/shape-the-solution`."
license: CC-BY-4.0
metadata:
  agent: solution-architect
  agent-version: "1"
---

# Record what the run taught

## What it does

Files what a shaping run or a proof taught: what the result corrected in
the shape, and what to do differently the next time the same problem
comes round.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/sls/shape-the-solution`, activity 15 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Record the Result and What It Taught**
  - `ref/sls/run-a-proof-of-value`, activity 15 -
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
