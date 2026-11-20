---
name: run-the-survey-period
description: Opens each survey period with its dates, its queues and the questions at their version, and closes it on its date with the count of cases closed, held back, surveyed and answered. Use it when running `ref/sup/survey-customers-after-a-case`.
license: CC-BY-4.0
metadata:
  agent: satisfaction-surveyor
  agent-version: "1"
---

# Run the survey period

## What it does

Opens each survey period with its dates, its queues and the questions at
their version, and closes it on its date with the count of cases closed,
held back, surveyed and answered.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Close the Survey Period**
  - `ref/sup/survey-customers-after-a-case`, activity 12 -
    [Survey Customers after a Case](../../../../processes/customer-support/survey-customers-after-a-case.md)
- **Open the Survey Period**
  - `ref/sup/survey-customers-after-a-case`, activity 1 -
    [Survey Customers after a Case](../../../../processes/customer-support/survey-customers-after-a-case.md)

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
