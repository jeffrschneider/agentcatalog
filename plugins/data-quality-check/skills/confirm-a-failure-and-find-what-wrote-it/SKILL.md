---
name: confirm-a-failure-and-find-what-wrote-it
description: Takes in a failing rule and re-runs it to see whether the failure is in the data or in the query behind it. Use it when running `ref/rev/fix-a-data-quality-failure`.
license: CC-BY-4.0
metadata:
  agent: data-quality-check
  agent-version: "1"
---

# Confirm a failure and find what wrote it

## What it does

Takes in a failing rule and re-runs it to see whether the failure is in
the data or in the query behind it. Then measures how far it spread,
finds the day it started, and traces it back to the form, the import,
the link or the person that wrote the bad values.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Check the Failure Is Real**
  - `ref/rev/fix-a-data-quality-failure`, activity 2 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Measure How Far It Spread**
  - `ref/rev/fix-a-data-quality-failure`, activity 3 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Take in the Failing Rule**
  - `ref/rev/fix-a-data-quality-failure`, activity 1 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)
- **Trace It to Its Source**
  - `ref/rev/fix-a-data-quality-failure`, activity 5 -
    [Fix a Data Quality Failure](../../../../processes/revenue-operations/fix-a-data-quality-failure.md)

## What to record

Per rule: the rule at a version, split into refuse, warn and report, and
the count of records already held that would fail it with the kinds of
record they are. The date it went live, and the failing count on its
cadence until the backfill deadline. Per failure: which rule, what it
measures, since when it has been failing and how far past its threshold
it sits; the re-run that showed whether the failure was in the data or
in the query; the failing records by object, owner and date; the day it
first failed set beside what shipped that week; the system, form or
person that wrote the failing values, with the evidence that it was that
one; the rule's result on the corrected records and on the records
written since the source was fixed; and the rule read on its cadence
across the watch period. A rule changed or retired lands at a new
version with the reason written down. Per merge: the record counts, the
related record counts and the affected reports read before and after,
with anything that did not reconcile.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
