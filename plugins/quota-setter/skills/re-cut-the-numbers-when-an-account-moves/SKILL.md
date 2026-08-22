---
name: re-cut-the-numbers-when-an-account-moves
description: Sets the date a moved account counts from, splits the credit either side of it, names what the move does to both sellers and their numbers, and records it against the carve. Use it when running `ref/rev/move-an-account`.
license: CC-BY-4.0
metadata:
  agent: quota-setter
  agent-version: "1"
---

# Re cut the numbers when an account moves

## What it does

Sets the date a moved account counts from, splits the credit either side
of it, names what the move does to both sellers and their numbers, and
records it against the carve. A move that shifts a receiving number by
more than the carve allows goes back to whoever decided it.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Name the Effect on Both Quotas**
  - `ref/rev/move-an-account`, activity 9 -
    [Move an Account](../../../../processes/revenue-operations/move-an-account.md)
- **Record the Move Against the Carve**
  - `ref/rev/move-an-account`, activity 14 -
    [Move an Account](../../../../processes/revenue-operations/move-an-account.md)
- **Set the Date It Counts From**
  - `ref/rev/move-an-account`, activity 7 -
    [Move an Account](../../../../processes/revenue-operations/move-an-account.md)
- **Split the Credit**
  - `ref/rev/move-an-account`, activity 8 -
    [Move an Account](../../../../processes/revenue-operations/move-an-account.md)

## What to record

Per run: the over-assignment as a figure with who decided it and why, a
draft on every patch naming the carrying figure and the curve behind it,
and the capacity test and the history test attached to each number.
Every number further from history than the stated distance carries the
reason for the difference beside it. The roll-up states the sum, the
target and the distance between them as an amount, and any adjustment
records what moved, on which patch, and by how much. Ramped numbers name
the written rule that produced them and the dates they cover. The signed
set names the person who signed it and the hour, and a quota changed
afterwards is a new version saying what moved and who decided it, with
the version it replaces left where it was.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
