---
name: group-outcome-check
description: Compares outcomes across groups, such as pay for like work, the selection for a layoff, or representation, hiring and leaving, on data a named person released for that check alone, and says which differences are larger than the noise. Use it when running `ref/hr/report-on-the-workforce`, `ref/hr/run-a-layoff` and `ref/hr/run-the-pay-review`.
license: CC-BY-4.0
metadata:
  agent: statistician
  agent-version: "1"
---

# Group outcome check

## What it does

Compares outcomes across groups, such as pay for like work, the
selection for a layoff, or representation, hiring and leaving, on data a
named person released for that check alone, and says which differences
are larger than the noise. It reports only groups at or above the
minimum size and never a result about one person, and named people
decide what follows.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Check the Selection Across Groups**
  - `ref/hr/run-a-layoff`, activity 10 -
    [Run a Layoff](../../../../processes/human-resources/run-a-layoff.md)
- **Compare Pay Across Groups**
  - `ref/hr/run-the-pay-review`, activity 11 -
    [Run the Pay Review](../../../../processes/human-resources/run-the-pay-review.md)
- **Work Out the Group Figures**
  - `ref/hr/report-on-the-workforce`, activity 9 -
    [Report on the Workforce](../../../../processes/human-resources/report-on-the-workforce.md)

## What to record

Before any data is gathered, the amount the study needs: how many
responses or how long the test has to run, what that number was computed
from, and the date it was said. Every figure with the data it was
computed from, the method it was computed with, and the range around it,
so the figure can be worked out again. Every exclusion, naming the rule
that removed the records, how many records it removed, and what the
figure looks like with them left in. Every weighting, naming which group
was weighted, to what, and against which reference. For each comparison,
a verdict saying whether the difference is larger than the noise at the
threshold the study set, with the size of the difference and the range
around it written beside the verdict. A list of every figure it could
not compute with the data it had, marked as such and carried into the
report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
