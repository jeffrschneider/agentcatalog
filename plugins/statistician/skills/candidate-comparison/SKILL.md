---
name: candidate-comparison
description: Sets the finalists for a purchase side by side on one sheet, using their scores, what the trial on real work showed and what each would cost. Use it when running `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: statistician
  agent-version: "1"
---

# Candidate comparison

## What it does

Sets the finalists for a purchase side by side on one sheet, using their
scores, what the trial on real work showed and what each would cost.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Compare the Finalists**
  - `ref/mkt/select-marketing-technology`, activity 16 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)
- **Try the Finalists on Real Work**
  - `ref/mkt/select-marketing-technology`, activity 14 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)

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
