---
name: tracking-links
description: Builds the coded links and parameters that let a visit be attributed to where it came from, so each advertisement, each creator and each destination can be counted separately in the report that reads them. Use it when running `ref/mkt/customer-reviews`, `ref/mkt/influencer-campaign` and `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Tracking links

## What it does

Builds the coded links and parameters that let a visit be attributed to
where it came from, so each advertisement, each creator and each
destination can be counted separately in the report that reads them.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Build the Tracking Parameters**
  - `ref/mkt/traffic-ad-creative`, activity 9 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Set up the Practical Side**
  - `ref/mkt/customer-reviews`, activity 9 -
    [Solicit Customer Reviews](../../../../processes/marketing/customer-reviews.md)
- **Set up the Tracking**
  - `ref/mkt/influencer-campaign`, activity 9 -
    [Run Influencer Campaign](../../../../processes/marketing/influencer-campaign.md)

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
