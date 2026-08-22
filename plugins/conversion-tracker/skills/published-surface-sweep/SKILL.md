---
name: published-surface-sweep
description: Finds every live page, advertisement and asset that carries a figure that has changed, such as a price, and gets each one restated so nothing still published contradicts the new one. Use it when running `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Published surface sweep

## What it does

Finds every live page, advertisement and asset that carries a figure
that has changed, such as a price, and gets each one restated so nothing
still published contradicts the new one.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Restate the Price Everywhere It Is Published**
  - `ref/mkt/pricing-change`, activity 7 -
    [Launch Pricing Change](../../../../processes/marketing/pricing-change.md)

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
