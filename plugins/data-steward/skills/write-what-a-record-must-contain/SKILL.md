---
name: write-what-a-record-must-contain
description: Takes in a request to define an object, reads who uses it today and what counts off it, and writes what the object means and what it is not. Use it when running `ref/rev/define-a-record`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Write what a record must contain

## What it does

Takes in a request to define an object, reads who uses it today and what
counts off it, and writes what the object means and what it is not. Then
the fields it carries, the ones a record may not be saved without, the
values each of those takes, and the fields that make two records the
same real thing.

## Where it happens

The agent does this in seven activities across one reference process.
Each one names the activity as that process words it.

- **Decide the Required Fields**
  - `ref/rev/define-a-record`, activity 5 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Fix the Allowed Values**
  - `ref/rev/define-a-record`, activity 6 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **List the Fields It Carries**
  - `ref/rev/define-a-record`, activity 4 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Read How the Record Is Used Today**
  - `ref/rev/define-a-record`, activity 2 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Set the Uniqueness Key**
  - `ref/rev/define-a-record`, activity 7 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Take in the Definition Request**
  - `ref/rev/define-a-record`, activity 1 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Write What the Object Means**
  - `ref/rev/define-a-record`, activity 3 -
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
