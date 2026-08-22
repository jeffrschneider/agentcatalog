---
name: check-the-tracking
description: Where touches went uncounted, and for how long. Use it when running `ref/mkt/attribution-model` and `ref/mkt/marketing-performance-report`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Check the Tracking

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/attribution-model`, where touches went uncounted, and for
  how long
- in `ref/mkt/marketing-performance-report`, where measurement was
  broken and for how long

## Where it happens

- `ref/mkt/attribution-model`, activity 5 -
  [Maintain Attribution Model](../../../../processes/marketing/attribution-model.md)
- `ref/mkt/marketing-performance-report`, activity 8 -
  [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)

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
