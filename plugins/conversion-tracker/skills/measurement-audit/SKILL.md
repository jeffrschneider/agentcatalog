---
name: measurement-audit
description: Reads the measurement data itself and says how far it can be trusted, which means where touches went uncounted and for how long, and whether the figures behind a signal are real and current. Use it when running `ref/mkt/attribution-model`, `ref/mkt/marketing-performance-report` and `ref/mkt/reallocate-media-spend`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Measurement audit

## What it does

Reads the measurement data itself and says how far it can be trusted,
which means where touches went uncounted and for how long, and whether
the figures behind a signal are real and current.

## Where it happens

The agent does this in two activities across three reference processes.
Each one names the activity as that process words it.

- **Check the Tracking**
  - `ref/mkt/attribution-model`, activity 5 -
    [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
  - `ref/mkt/marketing-performance-report`, activity 8 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Confirm the Numbers Hold**
  - `ref/mkt/reallocate-media-spend`, activity 2 -
    [Reallocate Media Spend](../../../../processes/marketing/reallocate-media-spend.md)

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
