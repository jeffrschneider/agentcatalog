---
name: figures-and-differences
description: Works out each figure with the range around it, and says whether a difference is larger than the noise in the measurement, whether that difference is between two groups, between this reading and the last one, or between what was expected and what happened. Use it when running `ref/mkt/analyze-customer-base` and 7 other reference processes.
license: CC-BY-4.0
metadata:
  agent: statistician
  agent-version: "1"
---

# Figures and differences

## What it does

Works out each figure with the range around it, and says whether a
difference is larger than the noise in the measurement, whether that
difference is between two groups, between this reading and the last one,
or between what was expected and what happened.

## Where it happens

The agent does this in seven activities across eight reference
processes. Each one names the activity as that process words it.

- **Compare with the Earlier Waves**
  - `ref/mkt/brand-health`, activity 17 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
- **Compare with the Last Read**
  - `ref/mkt/analyze-customer-base`, activity 13 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Name the Gaps Worth Acting On**
  - `ref/mkt/quarterly-business-review`, activity 7 -
    [Conduct Quarterly Business Review](../../../../processes/marketing/quarterly-business-review.md)
- **Read the Result**
  - `ref/mkt/conversion-experiment`, activity 13 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Test Whether the Segments Hold Apart**
  - `ref/mkt/segment-the-market`, activity 8 -
    [Segment the Market](../../../../processes/marketing/segment-the-market.md)
- **Test that the Groups Hold**
  - `ref/mkt/analyze-customer-base`, activity 9 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)
- **Work out the Figures**
  - `ref/mkt/brand-audit`, activity 12 -
    [Conduct Brand Audit](../../../../processes/marketing/brand-audit.md)
  - `ref/mkt/brand-health`, activity 16 -
    [Measure Brand Health](../../../../processes/marketing/brand-health.md)
  - `ref/mkt/customer-research`, activity 16 -
    [Conduct Customer Research](../../../../processes/marketing/customer-research.md)
  - `ref/mkt/win-loss-analysis`, activity 16 -
    [Conduct Win/Loss Analysis](../../../../processes/marketing/win-loss-analysis.md)

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
