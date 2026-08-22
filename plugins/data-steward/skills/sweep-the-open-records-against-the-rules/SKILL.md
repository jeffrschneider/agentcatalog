---
name: sweep-the-open-records-against-the-rules
description: Reads the rules as they are written, pulls the open records, and checks each one against what is priced, against who owns it and which territory and team it sits in, and against whether it is a duplicate or a split. Use it when running `ref/rev/enforce-pipeline-hygiene`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Sweep the open records against the rules

## What it does

Reads the rules as they are written, pulls the open records, and checks
each one against what is priced, against who owns it and which territory
and team it sits in, and against whether it is a duplicate or a split.
Fixes what the record can fix and marks what stays wrong rather than
quietly passing it.

## Where it happens

The agent does this in seven activities across one reference process.
Each one names the activity as that process words it.

- **Check Owner, Territory and Team**
  - `ref/rev/enforce-pipeline-hygiene`, activity 9 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Check the Amount Against What Is Priced**
  - `ref/rev/enforce-pipeline-hygiene`, activity 8 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Find the Duplicates and the Splits**
  - `ref/rev/enforce-pipeline-hygiene`, activity 10 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Fix What the Record Can Fix**
  - `ref/rev/enforce-pipeline-hygiene`, activity 13 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Mark the Deals That Stay Wrong**
  - `ref/rev/enforce-pipeline-hygiene`, activity 15 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Pull the Open Deals**
  - `ref/rev/enforce-pipeline-hygiene`, activity 4 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Read the Rules as Written**
  - `ref/rev/enforce-pipeline-hygiene`, activity 2 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)

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
