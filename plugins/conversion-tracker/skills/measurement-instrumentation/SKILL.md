---
name: measurement-instrumentation
description: Places the analytics tags on a page or a site and writes down which actions count as a result, so that traffic and what people do with it arrive in the reporting. Use it when running `ref/mkt/conversion-experiment` and 9 other reference processes.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Measurement instrumentation

## What it does

Places the analytics tags on a page or a site and writes down which
actions count as a result, so that traffic and what people do with it
arrive in the reporting. It respects the consent rules, so a tag fires
only where consent covers it.

## Where it happens

The agent does this in six activities across ten reference processes.
Each one names the activity as that process words it.

- **Settle What Counts as a Result**
  - `ref/mkt/media-plan`, activity 11 -
    [Develop Media Plan](../../../../processes/marketing/media-plan.md)
- **Tag the Site**
  - `ref/mkt/display-retargeting`, activity 6 -
    [Run Display Retargeting Campaign](../../../../processes/marketing/display-retargeting.md)
- **Wire the Measurement**
  - `ref/mkt/conversion-experiment`, activity 8 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)
- **Wire the Tracking**
  - `ref/mkt/landing-page`, activity 8 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)
- **Wire up Conversion Tracking**
  - `ref/mkt/paid-search-campaign`, activity 6 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)
- **Wire up the Measurement**
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
