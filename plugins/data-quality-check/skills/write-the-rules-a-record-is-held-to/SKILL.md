---
name: write-the-rules-a-record-is-held-to
description: Writes what the system refuses at save time, what it warns on and what it only reports later, holds that split at a version, runs it over the records already held to see what would fail, and turns it on with the failing count read on a cadence afterwards. Use it when running `ref/rev/define-a-record`.
license: CC-BY-4.0
metadata:
  agent: data-quality-check
  agent-version: "1"
---

# Write the rules a record is held to

## What it does

Writes what the system refuses at save time, what it warns on and what
it only reports later, holds that split at a version, runs it over the
records already held to see what would fail, and turns it on with the
failing count read on a cadence afterwards.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Test the Rules on Real Records**
  - `ref/rev/define-a-record`, activity 11 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Turn the Rules On**
  - `ref/rev/define-a-record`, activity 15 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Write the Rules That Enforce It**
  - `ref/rev/define-a-record`, activity 10 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)

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
