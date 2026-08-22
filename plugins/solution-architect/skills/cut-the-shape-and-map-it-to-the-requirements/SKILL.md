---
name: cut-the-shape-and-map-it-to-the-requirements
description: Cuts the shape down to what can actually be built, then sets it against the requirements one at a time so every requirement comes out met, deferred or refused. Use it when running `ref/sls/record-the-requirements`, `ref/sls/respond-to-an-rfp` and `ref/sls/shape-the-solution`.
license: CC-BY-4.0
metadata:
  agent: solution-architect
  agent-version: "1"
---

# Cut the shape and map it to the requirements

## What it does

Cuts the shape down to what can actually be built, then sets it against
the requirements one at a time so every requirement comes out met,
deferred or refused. Every refusal carries a reason, and a requirement
that cannot be met at all is said plainly before anything is shaped
around it.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Answer the Requirements**
  - `ref/sls/respond-to-an-rfp`, activity 7 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Cut It to What Is Buildable**
  - `ref/sls/shape-the-solution`, activity 9 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Map the Shape to the Requirements**
  - `ref/sls/shape-the-solution`, activity 10 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Mark What Cannot Be Met**
  - `ref/sls/record-the-requirements`, activity 9 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)

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
