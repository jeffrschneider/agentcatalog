---
name: break-the-results-down
description: The agent cuts a period's results by channel, topic, plan and hour of arrival until the cuts show a cause, sets each result beside the periods before it with the direction and the size of the change, and names no person in any cut. Use it when running `ref/sup/report-the-service-levels` and `ref/sup/report-what-customers-say`.
license: CC-BY-4.0
metadata:
  agent: analytics
  agent-version: "1"
---

# Break the results down

## What it does

The agent cuts a period's results by channel, topic, plan and hour of
arrival until the cuts show a cause, sets each result beside the periods
before it with the direction and the size of the change, and names no
person in any cut.

## Where it happens

The agent does this in four activities across two reference processes.
Each one names the activity as that process words it.

- **Break the Misses Down**
  - `ref/sup/report-the-service-levels`, activity 7 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Compare with the Period Before**
  - `ref/sup/report-the-service-levels`, activity 9 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Find the Cause Behind the Misses**
  - `ref/sup/report-the-service-levels`, activity 8 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Read the Trends**
  - `ref/sup/report-what-customers-say`, activity 3 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)

## What to record

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
