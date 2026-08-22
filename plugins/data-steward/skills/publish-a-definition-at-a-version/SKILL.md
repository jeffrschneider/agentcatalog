---
name: publish-a-definition-at-a-version
description: Puts the version in front of the object owner with the failing count and the breakage list attached, publishes it once a person signs, and sets the date by which the records already failing must be put right. Use it when running `ref/rev/define-a-record`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Publish a definition at a version

## What it does

Puts the version in front of the object owner with the failing count and
the breakage list attached, publishes it once a person signs, and sets
the date by which the records already failing must be put right. The
version it replaces stays readable at its own number.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Publish the Definition**
  - `ref/rev/define-a-record`, activity 14 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Set the Backfill Deadline**
  - `ref/rev/define-a-record`, activity 16 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Sign the Definition**
  - `ref/rev/define-a-record`, activity 13 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)

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
