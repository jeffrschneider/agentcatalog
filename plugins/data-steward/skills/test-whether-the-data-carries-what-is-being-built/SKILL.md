---
name: test-whether-the-data-carries-what-is-being-built
description: "Reads the fields a report, a rule or a clock is about to rest on and says whether they hold up: how full each one is, where the times come from, and whether the timestamps can carry the measure being asked of them. Use it when running `ref/rev/build-a-report`, `ref/rev/watch-the-response-clock` and `ref/rev/write-a-routing-rule`."
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Test whether the data carries what is being built

## What it does

Reads the fields a report, a rule or a clock is about to rest on and
says whether they hold up: how full each one is, where the times come
from, and whether the timestamps can carry the measure being asked of
them.

## Where it happens

The agent does this in five activities across three reference processes.
Each one names the activity as that process words it.

- **Check the Data Holds Up**
  - `ref/rev/write-a-routing-rule`, activity 5 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Check the Data Is There**
  - `ref/rev/build-a-report`, activity 5 -
    [Build a Report](../../../../processes/revenue-operations/build-a-report.md)
- **Check the Timestamps Hold Up**
  - `ref/rev/watch-the-response-clock`, activity 4 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
- **Read Where the Times Come From**
  - `ref/rev/watch-the-response-clock`, activity 3 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
- **Read the Fields the Rule Will Use**
  - `ref/rev/write-a-routing-rule`, activity 4 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)

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
