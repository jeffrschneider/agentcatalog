---
name: settle-the-shape-with-the-buyer
description: Walks the buyer through the shape, takes their corrections in their own words, and answers the follow-up questions and the presentation a bid asks for. Use it when running `ref/sls/respond-to-an-rfp` and `ref/sls/shape-the-solution`.
license: CC-BY-4.0
metadata:
  agent: solution-architect
  agent-version: "1"
---

# Settle the shape with the buyer

## What it does

Walks the buyer through the shape, takes their corrections in their own
words, and answers the follow-up questions and the presentation a bid
asks for. The run ends with one shape both sides agree to at a version.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Agree the Shape**
  - `ref/sls/shape-the-solution`, activity 14 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Handle Clarifications**
  - `ref/sls/respond-to-an-rfp`, activity 16 -
    [Respond to an RFP](../../../../processes/sales/respond-to-an-rfp.md)
- **Show the Shape to the Buyer**
  - `ref/sls/shape-the-solution`, activity 11 -
    [Shape the Solution](../../../../processes/sales/shape-the-solution.md)
- **Take the Buyer's Corrections**
  - `ref/sls/shape-the-solution`, activity 12 -
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
