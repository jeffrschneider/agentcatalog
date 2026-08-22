---
name: fill-a-field-and-stamp-where-it-came-from
description: Takes the records missing what the definition requires and fills the empty fields, stamping every value with its source, its date and the confidence behind it. Use it when running `ref/rev/enrich-a-record`.
license: CC-BY-4.0
metadata:
  agent: enrichment-operator
  agent-version: "1"
---

# Fill a field and stamp where it came from

## What it does

Takes the records missing what the definition requires and fills the
empty fields, stamping every value with its source, its date and the
confidence behind it. A value a person typed is never overwritten, and
the source's answer sits beside it as a disagreement instead.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Fill the Fields**
  - `ref/rev/enrich-a-record`, activity 8 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Leave Typed Values Alone**
  - `ref/rev/enrich-a-record`, activity 10 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Stamp Every Filled Field**
  - `ref/rev/enrich-a-record`, activity 9 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Take in the Thin Records**
  - `ref/rev/enrich-a-record`, activity 1 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)

## What to record

Per fill: the records below the bar, and which required fields were
empty on each. The sources chosen, the fields each one was to answer,
and what each cost per record. The sample filled from every source
beside the values already known to be right, and per source and per
field the agreement rate, the empty rate and the confidently wrong rate.
The precedence per field, and the confidence below which nothing is
written. Every field it wrote, carrying the source, the date it was
filled and the confidence the source returned. Every place a person had
typed something different, with the source's answer stored beside the
typed value as a disagreement rather than over it. Everything held back,
and what a person accepted, edited or rejected. What stayed empty,
reported as empty, and what was not attempted when a batch stopped. A
run that is abandoned still leaves its stamps, so a partial fill is
readable rather than mysterious.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
