---
name: compare-with-the-last-read
description: What moved since the read before this one. Use it when running `ref/mkt/analyze-customer-base`.
license: CC-BY-4.0
metadata:
  agent: statistician
  agent-version: "1"
---

# Compare with the Last Read

## What happens

What moved since the read before this one.

## Where it happens

- `ref/mkt/analyze-customer-base`, activity 13 -
  [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)

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
