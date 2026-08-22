---
name: list-what-is-still-open-at-an-ending
description: Lists every customer the partner holds and every piece of work still in flight before anything is closed, names what is still open as the portal, the systems, the price lists and the leads are closed off, and confirms the exit by naming anything nobody could close. Use it when running `ref/prt/end-a-partner-relationship`.
license: CC-BY-4.0
metadata:
  agent: partner-monitor
  agent-version: "1"
---

# List what is still open at an ending

## What it does

Lists every customer the partner holds and every piece of work still in
flight before anything is closed, names what is still open as the
portal, the systems, the price lists and the leads are closed off, and
confirms the exit by naming anything nobody could close.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Close Off the Access**
  - `ref/prt/end-a-partner-relationship`, activity 14 -
    [End a Partner Relationship](../../../../processes/partners/end-a-partner-relationship.md)
- **Confirm the Exit Is Complete**
  - `ref/prt/end-a-partner-relationship`, activity 16 -
    [End a Partner Relationship](../../../../processes/partners/end-a-partner-relationship.md)
- **List the Customers the Partner Holds**
  - `ref/prt/end-a-partner-relationship`, activity 5 -
    [End a Partner Relationship](../../../../processes/partners/end-a-partner-relationship.md)
- **List the Work in Flight**
  - `ref/prt/end-a-partner-relationship`, activity 6 -
    [End a Partner Relationship](../../../../processes/partners/end-a-partner-relationship.md)

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
