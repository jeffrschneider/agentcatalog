---
name: report-the-scores
description: Sets the period's scores beside the last period with the statistician agent's word on the noise, reports them by team, topic and channel to the support leaders, and brings them into the report of what customers say with no specialist named. Use it when running `ref/sup/report-what-customers-say` and `ref/sup/survey-customers-after-a-case`.
license: CC-BY-4.0
metadata:
  agent: satisfaction-surveyor
  agent-version: "1"
---

# Report the scores

## What it does

Sets the period's scores beside the last period with the statistician
agent's word on the noise, reports them by team, topic and channel to
the support leaders, and brings them into the report of what customers
say with no specialist named.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Compare with the Last Period**
  - `ref/sup/survey-customers-after-a-case`, activity 14 -
    [Survey Customers after a Case](../../../../processes/customer-support/survey-customers-after-a-case.md)
- **Report the Period's Scores**
  - `ref/sup/survey-customers-after-a-case`, activity 16 -
    [Survey Customers after a Case](../../../../processes/customer-support/survey-customers-after-a-case.md)
- **Take In the Survey Results**
  - `ref/sup/report-what-customers-say`, activity 5 -
    [Report What Customers Say](../../../../processes/customer-support/report-what-customers-say.md)

## What to record

Each period leaves its dates, the queues it covered and the questions at
their version, every case that closed in it with whether it was
surveyed, held back with its reason, or left unsurveyed because a system
failed, each survey and each reminder sent, each answer joined to its
case, each low score and problem passed to a team lead with how it was
followed up or why the customer could not be reached, the counts at the
close, and the scores reported with their counts and the statistician
agent's word on each change. Each specialist's own results leave a
record of who saw them, which is that specialist and their team lead and
nobody else. Nothing in the record shows this agent surveying a customer
the consent record did not cover, asking a customer twice inside the
interval, naming a specialist in a report, or ranking the people who
handled the cases.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
