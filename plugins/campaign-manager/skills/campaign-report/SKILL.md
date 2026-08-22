---
name: campaign-report
description: Reports what a run did against what it was asked to do, with the cost of each result, and puts the report in front of the agents it names so they can confirm the figures before it issues. Use it when running `ref/mkt/account-based-play` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: campaign-manager
  agent-version: "1"
---

# Campaign report

## What it does

Reports what a run did against what it was asked to do, with the cost of
each result, and puts the report in front of the agents it names so they
can confirm the figures before it issues.

## Where it happens

The agent does this in five activities across four reference processes.
Each one names the activity as that process words it.

- **Account for the Campaigns**
  - `ref/mkt/marketing-performance-report`, activity 5 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Check the Account**
  - `ref/mkt/marketing-performance-report`, activity 12 -
    [Report Marketing Performance](../../../../processes/marketing/marketing-performance-report.md)
- **Report Engagement**
  - `ref/mkt/account-based-play`, activity 18 -
    [Run Account-Based Play](../../../../processes/marketing/account-based-play.md)
- **Report against the Goal**
  - `ref/mkt/paid-search-campaign`, activity 12 -
    [Run Paid Search Campaign](../../../../processes/marketing/paid-search-campaign.md)
- **Report the Win-Back**
  - `ref/mkt/win-back-campaign`, activity 19 -
    [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
