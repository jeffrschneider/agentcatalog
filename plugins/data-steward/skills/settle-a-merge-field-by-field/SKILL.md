---
name: settle-a-merge-field-by-field
description: Once somebody has confirmed two records are one thing, pulls what each one holds, settles which record survives and which value wins on every field, and stores what did not survive against the survivor. Use it when running `ref/rev/dedupe-and-merge`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Settle a merge field by field

## What it does

Once somebody has confirmed two records are one thing, pulls what each
one holds, settles which record survives and which value wins on every
field, and stores what did not survive against the survivor. That store
is the only reason a merge can be taken back at all.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Choose the Surviving Record**
  - `ref/rev/dedupe-and-merge`, activity 7 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Keep What the Loser Held**
  - `ref/rev/dedupe-and-merge`, activity 9 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Pull What Each Record Holds**
  - `ref/rev/dedupe-and-merge`, activity 3 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Settle Every Field**
  - `ref/rev/dedupe-and-merge`, activity 8 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Undo the Merge**
  - `ref/rev/dedupe-and-merge`, activity 16 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)

## What to record

Per definition: the request and who made it, who reads the object today
and what counts off it, the sentence saying what the object is and what
it is not, every field with its fill rate and whether anything reads it,
the required list with the reason each field is required, the allowed
values with what each one means, the uniqueness key written as fields
rather than as a feeling, and where every field's value comes from. Then
the count of records already held that would fail, the reports and
integrations that read a changed field, the signed version with its
signer and date, and the backfill deadline with its owner and the count
still failing when the run closed. Per correction: the old value, the
new value and the reason, for every record touched. Per failure: the
source named with the evidence that it was that one, and a failure that
could not be traced recorded as unexplained rather than as fixed. Per
merge: the surviving id with the reason it was chosen, the winning value
per field naming the record it came from, and every value that did not
survive, stored against the survivor and dated.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
