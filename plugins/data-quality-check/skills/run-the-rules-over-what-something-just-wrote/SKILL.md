---
name: run-the-rules-over-what-something-just-wrote
description: Runs the definition's rules over everything an enrichment wrote and holds back the fills that fall under the bar. Use it when running `ref/rev/dedupe-and-merge` and `ref/rev/enrich-a-record`.
license: CC-BY-4.0
metadata:
  agent: data-quality-check
  agent-version: "1"
---

# Run the rules over what something just wrote

## What it does

Runs the definition's rules over everything an enrichment wrote and
holds back the fills that fall under the bar. Reads the record counts,
the related record counts and the affected reports before and after a
merge, and says what did not move.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Merge Landed**
  - `ref/rev/dedupe-and-merge`, activity 14 -
    [Dedupe and Merge](../../../../processes/revenue-operations/dedupe-and-merge.md)
- **Hold Back the Weak Fills**
  - `ref/rev/enrich-a-record`, activity 11 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Run the Rules Over the Fill**
  - `ref/rev/enrich-a-record`, activity 12 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)

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
