---
name: wire-up-the-measurement
description: Link tracking and what counts as a conversion. Use it when running `ref/mkt/customer-newsletter` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Wire up the Measurement

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/customer-newsletter`, link tracking and what counts as a
  conversion
- in `ref/mkt/long-form-content`, tags, conversions, and the form into
  the CRM
- in `ref/mkt/nurture-sequence`, conversions, tracked links, and the
  path into the CRM
- in `ref/mkt/test-ad-creative`, one conversion, and a tag that
  separates variants
- in `ref/mkt/win-back-campaign`, what counts as a return, and the path
  into the CRM

## Where it happens

- `ref/mkt/customer-newsletter`, activity 10 -
  [Publish Customer Newsletter](../../../../processes/marketing/customer-newsletter.md)
- `ref/mkt/long-form-content`, activity 12 -
  [Produce Long-Form Content](../../../../processes/marketing/long-form-content.md)
- `ref/mkt/nurture-sequence`, activity 8 -
  [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- `ref/mkt/test-ad-creative`, activity 11 -
  [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)
- `ref/mkt/win-back-campaign`, activity 9 -
  [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

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
