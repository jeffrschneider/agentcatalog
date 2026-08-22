---
name: put-a-rule-in-place-and-tighten-it
description: Puts a rule into the system once the fields behind it hold up, and changes it when the same thing keeps coming back. Use it when running `ref/rev/enforce-pipeline-hygiene`, `ref/rev/fix-a-data-quality-failure` and `ref/rev/write-a-routing-rule`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Put a rule in place and tighten it

## What it does

Puts a rule into the system once the fields behind it hold up, and
changes it when the same thing keeps coming back. A rule that has to be
tightened or amended lands at a new version with the reason written
down.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Amend the Rules from What Recurred**
  - `ref/rev/enforce-pipeline-hygiene`, activity 17 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Implement the Rule**
  - `ref/rev/write-a-routing-rule`, activity 13 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Tighten the Rule**
  - `ref/rev/fix-a-data-quality-failure`, activity 14 -
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
