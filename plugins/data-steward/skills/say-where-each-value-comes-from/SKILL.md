---
name: say-where-each-value-comes-from
description: Says where every field's value comes from, which source wins when two disagree, and the one system a number is read from. Use it when running `ref/rev/define-a-measure`, `ref/rev/define-a-record` and `ref/rev/enrich-a-record`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Say where each value comes from

## What it does

Says where every field's value comes from, which source wins when two
disagree, and the one system a number is read from. A value a person
typed is left where it is.

## Where it happens

The agent does this in five activities across three reference processes.
Each one names the activity as that process words it.

- **Leave Typed Values Alone**
  - `ref/rev/enrich-a-record`, activity 10 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Name the Source of Record**
  - `ref/rev/define-a-measure`, activity 6 -
    [Define a Measure](../../../../processes/revenue-operations/define-a-measure.md)
- **Read the Field Definitions**
  - `ref/rev/enrich-a-record`, activity 2 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Say Where Each Field Comes From**
  - `ref/rev/define-a-record`, activity 8 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Set Which Source Wins**
  - `ref/rev/enrich-a-record`, activity 7 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)

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
