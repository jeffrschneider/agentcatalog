---
name: page-experiments
description: Sets what a page test changes, who sees it and which measure decides it, watches delivery and the guardrail measures while it runs, and puts the answer into effect by rolling one version out to everyone or taking the change back out. Use it when running `ref/mkt/conversion-experiment`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Page experiments

## What it does

Sets what a page test changes, who sees it and which measure decides it,
watches delivery and the guardrail measures while it runs, and puts the
answer into effect by rolling one version out to everyone or taking the
change back out.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Carry out the Decision**
  - `ref/mkt/conversion-experiment`, activity 15 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Set the Terms of the Test**
  - `ref/mkt/conversion-experiment`, activity 2 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Watch the Test Run**
  - `ref/mkt/conversion-experiment`, activity 12 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)

## What to record

A measurement plan at a version, naming every conversion, what counts as
one, and where it fires. For each conversion, a dated test record
showing a real submission arriving in the CRM. The tracking parameters
it handed to each paid channel, recorded against the page they belong
to. Anything it could not verify is recorded as unverified rather than
left out.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
