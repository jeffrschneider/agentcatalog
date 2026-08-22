---
name: page-and-form-build
description: Builds the page a run points people at, together with the form on it, and puts the measurement on both before anyone is sent there. Use it when running `ref/mkt/account-based-play` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Page and form build

## What it does

Builds the page a run points people at, together with the form on it,
and puts the measurement on both before anyone is sent there.

## Where it happens

The agent does this in three activities across four reference processes.
Each one names the activity as that process words it.

- **Build the Pages and the Notice**
  - `ref/mkt/account-based-play`, activity 13 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Build the Registration Page**
  - `ref/mkt/webinar`, activity 4 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)
- **Open Registration**
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
