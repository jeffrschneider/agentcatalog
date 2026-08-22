---
name: confirm-the-drift
description: Test the gap against a holdout before rebuilding. Use it when running `ref/mkt/attribution-model`.
license: CC-BY-4.0
metadata:
  agent: statistician
  agent-version: "1"
---

# Confirm the Drift

## What happens

Test the gap against a holdout before rebuilding.

## Where it happens

- `ref/mkt/attribution-model`, activity 2 -
  [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)

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
