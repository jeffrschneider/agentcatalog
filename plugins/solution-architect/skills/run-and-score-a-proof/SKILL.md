---
name: run-and-score-a-proof
description: Stands the environment up, watches the proof while it runs, holds the check partway through, and scores the result line by line against the criteria agreed at the start. Use it when running `ref/sls/run-a-proof-of-value`.
license: CC-BY-4.0
metadata:
  agent: solution-architect
  agent-version: "1"
---

# Run and score a proof

## What it does

Stands the environment up, watches the proof while it runs, holds the
check partway through, and scores the result line by line against the
criteria agreed at the start. The closing review is held with both sides
in the room.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Hold the Closing Review**
  - `ref/sls/run-a-proof-of-value`, activity 13 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)
- **Hold the Midpoint Check**
  - `ref/sls/run-a-proof-of-value`, activity 11 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)
- **Score Against the Criteria**
  - `ref/sls/run-a-proof-of-value`, activity 12 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)
- **Set Up the Environment**
  - `ref/sls/run-a-proof-of-value`, activity 7 -
    [Run a Proof of Value](../../../../processes/sales/run-a-proof-of-value.md)
- **Watch It While It Runs**
  - `ref/sls/run-a-proof-of-value`, activity 10 -
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
