---
name: carry-what-stays-wrong-into-the-numbers
description: Marks the deals that still fail after their owner has been told, hands those marks to the arithmetic downstream, and marks the figures on the published view that the data cannot carry. Use it when running `ref/rev/build-the-roll-up`, `ref/rev/enforce-pipeline-hygiene` and `ref/rev/publish-the-forecast-view`.
license: CC-BY-4.0
metadata:
  agent: pipeline-check
  agent-version: "1"
---

# Carry what stays wrong into the numbers

## What it does

Marks the deals that still fail after their owner has been told, hands
those marks to the arithmetic downstream, and marks the figures on the
published view that the data cannot carry. A failing deal is flagged and
stays in the count. It is never dropped to make a report look better.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Mark the Deals That Stay Wrong**
  - `ref/rev/enforce-pipeline-hygiene`, activity 15 -
    [Enforce Pipeline Hygiene](../../../../processes/revenue-operations/enforce-pipeline-hygiene.md)
- **Mark the Figures the Data Cannot Carry**
  - `ref/rev/publish-the-forecast-view`, activity 8 -
    [Publish the Forecast View](../../../../processes/revenue-operations/publish-the-forecast-view.md)
- **Take in the Hygiene Marks**
  - `ref/rev/build-the-roll-up`, activity 5 -
    [Build the Roll-Up](../../../../processes/revenue-operations/build-the-roll-up.md)

## What to record

Per run: the rules and stage definitions at the version they were read
at, the extract every check ran against, and the staleness numbers with
who agreed them. Per finding: the deal, the rule it failed, the amount
it moves, the person it was sent to and the date it was sent. Withdrawn
findings are kept as withdrawn with the reason, and a dispute is kept
whether or not the finding stood, because a rule many owners dispute is
the next amendment. Every mark carried into the roll-up names its rule
and its date. Somebody auditing a run can replay each finding against
the extract behind it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
