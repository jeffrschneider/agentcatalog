---
name: run-a-controlled-comparison
description: "The agent sets up a fair comparison: how many versions run, how the traffic splits between them, where each one runs, how much exposure is needed, and how big a difference counts. Use it when running `ref/mkt/conversion-experiment` and `ref/mkt/test-ad-creative`."
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Run a controlled comparison

## What it does

The agent sets up a fair comparison: how many versions run, how the
traffic splits between them, where each one runs, how much exposure is
needed, and how big a difference counts. When it is over, the agent
reads the result and says how much of the difference is noise.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Design the Comparison**
  - `ref/mkt/test-ad-creative`, activity 4 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Read the Result**
  - `ref/mkt/conversion-experiment`, activity 13 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
  - `ref/mkt/test-ad-creative`, activity 15 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- **Set the Evidence Bar**
  - `ref/mkt/test-ad-creative`, activity 5 -
    [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
