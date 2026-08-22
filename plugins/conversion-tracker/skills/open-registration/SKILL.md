---
name: open-registration
description: The registration page, with its tracking wired up. Use it when running `ref/mkt/field-event` and `ref/mkt/user-conference`.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Open Registration

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/field-event`, the registration page, with its tracking
  wired up
- in `ref/mkt/user-conference`, the site, the sign-up and the tracking
  go live

## Where it happens

- `ref/mkt/field-event`, activity 8 -
  [Host Field Event](../../../../processes/marketing/field-event.md)
- `ref/mkt/user-conference`, activity 7 -
  [Host User Conference](../../../../processes/marketing/user-conference.md)

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
