---
name: wire-up-the-split
description: Tracking, the form fields, and where each lead goes. Use it when running `ref/mkt/co-marketing-campaign`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Wire up the Split

## What happens

Tracking, the form fields, and where each lead goes.

## Where it happens

- `ref/mkt/co-marketing-campaign`, activity 10 -
  [Run Co-Marketing Campaign](../../../../processes/marketing/co-marketing-campaign.md)

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
