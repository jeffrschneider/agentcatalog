---
name: page-verification
description: Reads a page after it is built or changed and confirms it works for a visitor and for the reporting, which covers the links, the headings, how it loads, whether it meets the accessibility standard, and whether the visit is recorded. Use it when running `ref/mkt/refresh-content`, `ref/mkt/traffic-ad-creative` and `ref/mkt/website-content-update`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Page verification

## What it does

Reads a page after it is built or changed and confirms it works for a
visitor and for the reporting, which covers the links, the headings, how
it loads, whether it meets the accessibility standard, and whether the
visit is recorded.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Check Every Destination**
  - `ref/mkt/traffic-ad-creative`, activity 10 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)
- **Check the Changed Page**
  - `ref/mkt/website-content-update`, activity 10 -
    [Update Website Content](../../../../processes/marketing/website-content-update.md)
- **Check the Changed Pages**
  - `ref/mkt/refresh-content`, activity 18 -
    [Refresh Published Content](../../../../processes/marketing/refresh-content.md)

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
