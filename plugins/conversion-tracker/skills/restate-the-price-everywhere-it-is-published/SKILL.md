---
name: restate-the-price-everywhere-it-is-published
description: Every live page, ad and asset that names a price. Use it when running `ref/mkt/pricing-change`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Restate the Price Everywhere It Is Published

## What happens

Every live page, ad and asset that names a price.

## Where it happens

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
