---
name: check-every-destination
description: The page each ad points at loads and records the visit. Use it when running `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Check Every Destination

## What happens

The page each ad points at loads and records the visit.

## Where it happens

- `ref/mkt/traffic-ad-creative`, activity 10 -
  [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

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
