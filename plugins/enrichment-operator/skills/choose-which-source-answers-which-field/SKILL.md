---
name: choose-which-source-answers-which-field
description: Reads what the definition asks each field to hold, says where each one comes from, picks the sources and the order they answer in, and tests a sample against records already known to be right before anything is bought or written at scale. Use it when running `ref/rev/define-a-record` and `ref/rev/enrich-a-record`.
license: CC-BY-4.0
metadata:
  agent: enrichment-operator
  agent-version: "1"
---

# Choose which source answers which field

## What it does

Reads what the definition asks each field to hold, says where each one
comes from, picks the sources and the order they answer in, and tests a
sample against records already known to be right before anything is
bought or written at scale.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Choose the Sources**
  - `ref/rev/enrich-a-record`, activity 4 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Say Where Each Field Comes From**
  - `ref/rev/define-a-record`, activity 8 -
    [Define a Record](../../../../processes/revenue-operations/define-a-record.md)
- **Set Which Source Wins**
  - `ref/rev/enrich-a-record`, activity 7 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Test a Sample First**
  - `ref/rev/enrich-a-record`, activity 5 -
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
