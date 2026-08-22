---
name: merge-two-records-into-one
description: Once a person confirms, chooses the surviving id and the reason it won, repoints the activities, deals, contacts and files at it, tells both owners before the merge rather than after, and closes the losing record pointing at the survivor. Use it when running `ref/rev/dedupe-and-merge`.
license: CC-BY-4.0
metadata:
  agent: deduper
  agent-version: "1"
---

# Merge two records into one

## What it does

Once a person confirms, chooses the surviving id and the reason it won,
repoints the activities, deals, contacts and files at it, tells both
owners before the merge rather than after, and closes the losing record
pointing at the survivor.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Choose the Surviving Record**
  - `ref/rev/dedupe-and-merge`, activity 7 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Confirm They Are One Thing**
  - `ref/rev/dedupe-and-merge`, activity 6 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Merge the Records**
  - `ref/rev/dedupe-and-merge`, activity 13 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Move the Related Records**
  - `ref/rev/dedupe-and-merge`, activity 10 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Tell the Owners**
  - `ref/rev/dedupe-and-merge`, activity 12 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)

## What to record

Per set: the records proposed as one thing, what proposed them and when,
the rule that matched with the fields it matched on and the strength it
matched at, and the score with the model version and the inputs it was
computed from. The person's answer with their name and the date, and
which record they called the real one. The surviving id and the reason
it was chosen over the other. Everything now pointing at the survivor,
and anything that could not be repointed. Both owners told, with the
date they were told. The merge as written, and the closed record
pointing at the survivor. Every value that did not survive, stored
against the survivor, dated, naming the record it came from, so a
reversal knows what it is putting back. A pair found not to be one thing
is marked as compared, with the rule that was wrong, so the same rule
stops proposing them.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
