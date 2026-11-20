---
name: check-the-record-holds-up
description: "Before a figure is counted or reported, the agent checks that the record under it holds up: stamps that are missing or back-dated, gaps in the history, and days such as an outage or a holiday that have to be read with care, each marked with its reason. Use it when running `ref/sup/forecast-support-volume`, `ref/sup/report-the-service-levels` and `ref/sup/report-what-customers-say`."
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Check the record holds up

## What it does

Before a figure is counted or reported, the agent checks that the record
under it holds up: stamps that are missing or back-dated, gaps in the
history, and days such as an outage or a holiday that have to be read
with care, each marked with its reason. Every figure in a finding is
traced to the system and the date it was read from, and a figure that
does not trace is read again.

## Where it happens

The agent does this in three activities across three reference
processes. Each one names the activity as that process words it.

- **Check Every Figure against Its Source**
  - `ref/sup/report-what-customers-say`, activity 9 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)
- **Check the Stamps Hold Up**
  - `ref/sup/report-the-service-levels`, activity 3 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Mark the Unusual Days**
  - `ref/sup/forecast-support-volume`, activity 3 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
