---
name: live-path-verification
description: Puts a real click, contact or session through the whole path once it is live and reports whether every step fired, from the advertisement rendering to the record arriving in the system that has to receive it. Use it when running `ref/mkt/conversion-experiment`, `ref/mkt/nurture-sequence` and `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Live path verification

## What it does

Puts a real click, contact or session through the whole path once it is
live and reports whether every step fired, from the advertisement
rendering to the record arriving in the system that has to receive it.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Check the Live Ads**
  - `ref/mkt/traffic-ad-creative`, activity 16 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Check the Setup**
  - `ref/mkt/conversion-experiment`, activity 10 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Run Test Contacts Through It**
  - `ref/mkt/nurture-sequence`, activity 12 -
    [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)

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
