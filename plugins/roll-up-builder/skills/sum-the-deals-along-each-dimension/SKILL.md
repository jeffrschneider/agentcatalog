---
name: sum-the-deals-along-each-dimension
description: Sums the same deals along whatever dimensions leadership asks for, and ties every cut back to the extract deal by deal. Use it when running `ref/rev/build-the-roll-up`.
license: CC-BY-4.0
metadata:
  agent: roll-up-builder
  agent-version: "1"
---

# Sum the deals along each dimension

## What it does

Sums the same deals along whatever dimensions leadership asks for, and
ties every cut back to the extract deal by deal. A difference is chased
until it is understood, never posted as a rounding line or an other row.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Reconcile the Cuts Against the Extract**
  - `ref/rev/build-the-roll-up`, activity 9 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)
- **Roll the Deals Up by Each Dimension**
  - `ref/rev/build-the-roll-up`, activity 8 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)

## What to record

The cut-off with its time zone, and the cut-off the last cycle used. The
extract with its row count and its total. Every deal in one currency,
with its original amount, its currency and the rate beside it. Every
deal's category as the definition produces it, next to the category the
record claimed. Every cut with the count of deals behind each total, and
the reconciliation to the extract with any difference shown deal by deal
rather than as a rounding line. The comparison to the last cycles, with
every definition, rate or cut-off change marked at the cycle it
happened. The questions this roll-up could not answer, each with the
reason. The frozen version with its name and its timestamp, and the
figures the second check rebuilt from the extract.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
