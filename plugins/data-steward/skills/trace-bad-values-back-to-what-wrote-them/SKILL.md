---
name: trace-bad-values-back-to-what-wrote-them
description: Follows failing values back to the form, the import, the link or the person that wrote them, names who owns that source, and gets a decision on whether it keeps writing while it is being fixed. Use it when running `ref/rev/define-a-record` and `ref/rev/fix-a-data-quality-failure`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Trace bad values back to what wrote them

## What it does

Follows failing values back to the form, the import, the link or the
person that wrote them, names who owns that source, and gets a decision
on whether it keeps writing while it is being fixed. Then the source is
put right, the records already wrong are corrected, and the failure
closes. A trail that runs cold closes as unexplained rather than as
fixed.

## Where it happens

The agent does this in seven activities across two reference processes.
Each one names the activity as that process words it.

- **Close the Failure**
  - `ref/rev/fix-a-data-quality-failure`, activity 15 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Correct the Records Already Wrong**
  - `ref/rev/fix-a-data-quality-failure`, activity 10 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Decide Whether to Stop the Flow**
  - `ref/rev/fix-a-data-quality-failure`, activity 7 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Fix It at the Source**
  - `ref/rev/fix-a-data-quality-failure`, activity 8 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Name Who Owns the Source**
  - `ref/rev/fix-a-data-quality-failure`, activity 6 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Record What Was Learned**
  - `ref/rev/define-a-record`, activity 17 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
  - `ref/rev/fix-a-data-quality-failure`, activity 16 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Trace It to Its Source**
  - `ref/rev/fix-a-data-quality-failure`, activity 5 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)

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
