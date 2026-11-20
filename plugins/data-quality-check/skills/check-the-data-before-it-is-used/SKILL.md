---
name: check-the-data-before-it-is-used
description: "Runs the rules over the data a filing, a tax return or a report is built from before anyone signs it: every record complete, consistent with the others, and agreeing with the system that keeps its own count, such as the headcount and pay totals in the payroll system, or the tax code, address and amount of each invoice behind a tax return. Use it when running `ref/fin/file-an-indirect-tax-return` and `ref/hr/file-a-required-report`."
license: CC-BY-4.0
metadata:
  agent: data-quality-check
  agent-version: "1"
---

# Check the data before it is used

## What it does

Runs the rules over the data a filing, a tax return or a report is built
from before anyone signs it: every record complete, consistent with the
others, and agreeing with the system that keeps its own count, such as
the headcount and pay totals in the payroll system, or the tax code,
address and amount of each invoice behind a tax return. Each failure is
listed with the records it failed on.

## Where it happens

The agent does this in one activity across two reference processes. Each
one names the activity as that process words it.

- **Check the Data**
  - `ref/fin/file-an-indirect-tax-return`, activity 4 -
    [File an Indirect Tax Return](../../../../processes/finance/file-an-indirect-tax-return.md)
  - `ref/hr/file-a-required-report`, activity 6 -
    [File a Required Report](../../../../processes/human-resources/file-a-required-report.md)

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
