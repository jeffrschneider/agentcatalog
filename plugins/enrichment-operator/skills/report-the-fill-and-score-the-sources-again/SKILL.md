---
name: report-the-fill-and-score-the-sources-again
description: Reports what was filled by source, what it cost, what disagreed with a typed value, and what stayed empty. Use it when running `ref/rev/enrich-a-record`.
license: CC-BY-4.0
metadata:
  agent: enrichment-operator
  agent-version: "1"
---

# Report the fill and score the sources again

## What it does

Reports what was filled by source, what it cost, what disagreed with a
typed value, and what stayed empty. Scores the sources again on a
cadence to catch one that has drifted since it was chosen, and files
which source is worth what it costs.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/rev/enrich-a-record`, activity 16 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Report the Fill**
  - `ref/rev/enrich-a-record`, activity 14 -
    [Enrich a Record](../../../../processes/revenue-operations/enrich-a-record.md)
- **Score the Sources Again**
  - `ref/rev/enrich-a-record`, activity 15 -
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
