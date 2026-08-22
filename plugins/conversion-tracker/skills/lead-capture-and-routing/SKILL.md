---
name: lead-capture-and-routing
description: Connects a form or a capture device to the systems that hold the records, decides which fields are taken and where each record goes, and delivers each record to whoever has to follow it up. Use it when running `ref/mkt/channel-program` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: conversion-tracker
  agent-version: "1"
---

# Lead capture and routing

## What it does

Connects a form or a capture device to the systems that hold the
records, decides which fields are taken and where each record goes, and
delivers each record to whoever has to follow it up.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Hand off the Leads**
  - `ref/mkt/webinar`, activity 16 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)
- **Set up Lead Capture**
  - `ref/mkt/trade-show`, activity 9 -
    [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)
- **Set up the Partner Systems**
  - `ref/mkt/channel-program`, activity 9 -
    [Launch Channel Program](../../../../processes/marketing/channel-program.md)
- **Wire up the Split**
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
