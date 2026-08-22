---
name: fix-the-boundary-a-number-is-cut-at
description: Fixes the edges a number is cut at, and keeps them fixed. Use it when running `ref/rev/build-a-report` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: data-steward
  agent-version: "1"
---

# Fix the boundary a number is cut at

## What it does

Fixes the edges a number is cut at, and keeps them fixed. That is what a
measure counts in and out, the cut-off a set of figures is pulled at,
the period a clock runs over, and the slice and the cadence a report is
read on.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Choose the Cut and the Cadence**
  - `ref/rev/build-a-report`, activity 6 -
    [Build a Report](../../../../processes/revenue-operations/build-a-report.md)
- **Fix the Cut-Off**
  - `ref/rev/build-the-roll-up`, activity 2 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)
- **Keep the Period**
  - `ref/rev/watch-the-response-clock`, activity 16 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
- **Set the Boundaries**
  - `ref/rev/define-a-measure`, activity 7 -
    [Define a Measure](../../../../processes/revenue-operations/define-a-measure.md)

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
