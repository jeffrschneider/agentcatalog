---
name: check-what-the-partner-actually-experiences
description: Checks the path as the partner meets it rather than as the record describes it. Use it when running `ref/prt/onboard-a-partner` and `ref/prt/set-a-partner-tier`.
license: CC-BY-4.0
metadata:
  agent: partner-monitor
  agent-version: "1"
---

# Check what the partner actually experiences

## What it does

Checks the path as the partner meets it rather than as the record
describes it. A test deal and a test ticket have to land, and the
entitlement a tier promises has to be the one the partner can actually
see.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Partner Sees the Right Thing**
  - `ref/prt/set-a-partner-tier`, activity 14 -
    [Set a Partner Tier](../../../../processes/partners/set-a-partner-tier.md)
- **Test the Path End to End**
  - `ref/prt/onboard-a-partner`, activity 13 -
    [Onboard a Partner](../../../../processes/partners/onboard-a-partner.md)

## What to record

For every reading: the period it covers, the measure set at its version,
the source of each number and the date it was pulled, so somebody else
can recompute it. What the partner owed and what the company owed, read
in the same round and reported together. Every difference between our
count and the partner's, marked settled or open, with what is missing.
Everything it could not read, marked unread and naming the data that was
not there. A dated line for every certificate that lapsed and every
certified person who left. At an ending, the list of customers the
partner holds, the work still in flight, and the confirmation that names
anything that could not be closed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
