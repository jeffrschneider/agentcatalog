---
name: read-the-result
description: The numbers, the difference, and how much is noise. Use it when running `ref/mkt/conversion-experiment` and `ref/mkt/test-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Read the Result

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/conversion-experiment`, the numbers, the difference, and
  how much is noise
- in `ref/mkt/test-ad-creative`, exposure, run length and the gap
  between variants

## Where it happens

- `ref/mkt/conversion-experiment`, activity 13 -
  [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- `ref/mkt/test-ad-creative`, activity 15 -
  [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
