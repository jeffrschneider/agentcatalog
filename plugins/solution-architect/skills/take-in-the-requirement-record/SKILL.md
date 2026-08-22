---
name: take-in-the-requirement-record
description: Picks up the requirement record at its version as recording hands it over, and reads the shapes drawn for similar problems before anything new is written. Use it when running `ref/sls/record-the-requirements`, `ref/sls/respond-to-an-rfp` and `ref/sls/shape-the-solution`.
license: CC-BY-4.0
metadata:
  agent: solution-architect
  agent-version: "1"
---

# Take in the requirement record

## What it does

Picks up the requirement record at its version as recording hands it
over, and reads the shapes drawn for similar problems before anything
new is written. Where the ask arrives as a formal bid, decides whether
it is worth answering and writes down the reason either way.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Decide Whether to Bid**
  - `ref/sls/respond-to-an-rfp`, activity 3 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Hand the Record to Shaping**
  - `ref/sls/record-the-requirements`, activity 12 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)
- **Read What Was Shaped Before**
  - `ref/sls/shape-the-solution`, activity 2 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Take in the Requirement Record**
  - `ref/sls/shape-the-solution`, activity 1 -
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
