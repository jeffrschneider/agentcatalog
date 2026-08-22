---
name: say-what-changed-and-what-was-left-out
description: Records a correction as a new version rather than editing the figure that already went out, and says plainly what an answer left out. Use it when running `ref/rev/answer-a-data-question` and `ref/rev/publish-the-forecast-view`.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Say what changed and what was left out

## What it does

Records a correction as a new version rather than editing the figure
that already went out, and says plainly what an answer left out. A
report can then name the version it was computed under.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Record Corrections as New Versions**
  - `ref/rev/publish-the-forecast-view`, activity 15 -
    [Publish the Forecast View](../../../../processes/revenue-operations/publish-the-forecast-view.md)
- **Say What Was Left Out**
  - `ref/rev/answer-a-data-question`, activity 8 -
    [Answer a Data Question](../../../../processes/revenue-operations/answer-a-data-question.md)

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
