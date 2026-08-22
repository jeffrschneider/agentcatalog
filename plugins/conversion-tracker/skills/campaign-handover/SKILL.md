---
name: campaign-handover
description: Hands the finished page to the run that will send traffic to it, with its address and the tracking that goes with it, so the campaign points at the right place and reads the right numbers. Use it when running `ref/mkt/landing-page`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Campaign handover

## What it does

Hands the finished page to the run that will send traffic to it, with
its address and the tracking that goes with it, so the campaign points
at the right place and reads the right numbers.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Hand It to the Campaign**
  - `ref/mkt/landing-page`, activity 12 -
    [Publish Landing Page](../../../../processes/marketing/landing-page.md)

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
