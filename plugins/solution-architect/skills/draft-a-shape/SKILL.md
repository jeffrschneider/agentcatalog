---
name: draft-a-shape
description: Draws the first shape in writing, so somebody can disagree with a sentence rather than with a whiteboard. Use it when running `ref/sls/respond-to-an-rfp` and `ref/sls/shape-the-solution`.
license: CC-BY-4.0
metadata:
  agent: solution-architect
  agent-version: "1"
---

# Draft a shape

## What it does

Draws the first shape in writing, so somebody can disagree with a
sentence rather than with a whiteboard. Checks every part of it against
what the product does today, keeping what ships apart from what is only
planned. The same drafting answers a bid that asks how the work would
actually be done.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check What the Product Does Today**
  - `ref/sls/shape-the-solution`, activity 4 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Design the Solution Response**
  - `ref/sls/respond-to-an-rfp`, activity 8 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Draft the First Shape**
  - `ref/sls/shape-the-solution`, activity 3 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)

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
