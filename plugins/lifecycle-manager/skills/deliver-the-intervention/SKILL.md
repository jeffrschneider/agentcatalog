---
name: deliver-the-intervention
description: The message goes out or the account owner calls. Use it when running `ref/mkt/churn-risk-play`.
license: CC-BY-4.0
metadata:
  agent: lifecycle-manager
  agent-version: "1"
---

# Deliver the Intervention

## What happens

The message goes out or the account owner calls.

## Where it happens

- `ref/mkt/churn-risk-play`, activity 9 -
  [Run Churn-Risk Play](../../../../processes/marketing/churn-risk-play.md)

## What to record

For each customer, the run at a version: the date they entered, the
condition that put them in, the goal the run is trying to reach, every
step they were given with the date and the reason it was chosen, and
every step that was skipped with the reason it was skipped. A dated line
each time the path changed, naming what changed and what the customer
did or failed to do that changed it. Every commitment made to the
customer, naming who made it, what was promised, when it is due, and the
date it was met. The handover record when a person takes over, saying
what that person is being asked to do and everything the customer has
already been sent. The closing record, saying whether the goal was
reached, what the customer did, and the date the run ended.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
