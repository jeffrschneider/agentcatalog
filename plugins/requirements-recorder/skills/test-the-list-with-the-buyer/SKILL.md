---
name: test-the-list-with-the-buyer
description: Finds the pairs that cannot both be met and puts them back to the buyer rather than settling them on the buyer's behalf. Use it when running `ref/sls/record-the-requirements`.
license: CC-BY-4.0
metadata:
  agent: requirements-recorder
  agent-version: "1"
---

# Test the list with the buyer

## What it does

Finds the pairs that cannot both be met and puts them back to the buyer
rather than settling them on the buyer's behalf. Has the buyer rank the
list, and marks the requirements that cannot be met, each with its
reason, before any shape is drawn.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Ask the Follow-Up Questions**
  - `ref/sls/record-the-requirements`, activity 6 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)
- **Find the Contradictions**
  - `ref/sls/record-the-requirements`, activity 5 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)
- **Have the Buyer Rank the List**
  - `ref/sls/record-the-requirements`, activity 8 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)
- **Mark What Cannot Be Met**
  - `ref/sls/record-the-requirements`, activity 9 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)

## What to record

One line per requirement, quoted in the buyer's words, with any
paraphrase marked as a paraphrase, the person who asked for it, and the
date they asked. The needs-and-wants split, with who drew the line. The
contradictions found, and what came back when each went to the buyer.
The buyer's ranking, recorded as the buyer's, with any seller re-ranking
kept beside it as a separate marked opinion. The requirements marked as
unmeetable, each with its reason and the date it was marked. The
read-back and the buyer's confirmation. The version number and its date,
with earlier versions still readable, and every later requirement
written, attributed and versioned in rather than absorbed quietly. The
mapping of shape to record, showing each requirement met, deferred or
refused.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
