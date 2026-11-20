---
name: publish-the-promise-and-the-result
description: Writes the promise and what actually happened side by side, whether the number is good or bad, and takes each queue its own number rather than the average. Use it when running `ref/rev/watch-the-response-clock` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: response-clock-monitor
  agent-version: "1"
---

# Publish the promise and the result

## What it does

Writes the promise and what actually happened side by side, whether the
number is good or bad, and takes each queue its own number rather than
the average. A new rule or a new schedule gets the same reading over its
first week, and each team lead is taken through their own queues.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Take Each Queue Its Own Number**
  - `ref/rev/watch-the-response-clock`, activity 14 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
- **Take Each Team Lead Through Their Queues**
  - `ref/sup/report-the-service-levels`, activity 13 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Watch the First Week**
  - `ref/rev/write-a-routing-rule`, activity 17 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
  - `ref/sup/build-the-support-schedule`, activity 17 -
    [Build the Support Schedule](../../../../processes/customer-support/build-the-support-schedule.md)
- **Write the Report**
  - `ref/rev/watch-the-response-clock`, activity 11 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
  - `ref/sup/report-the-service-levels`, activity 10 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)

## What to record

Per window: each clock with the event that starts it, the event that
stops it and the states that pause it, written so two people read them
the same way. One row per run with its start, its stop, its queue, its
owner and its elapsed time, marked met, missed, or open past its due
time. The set-aside list carries a written reason and the name of the
person who agreed on every line, and the set-aside count is published
next to the result. The misses are cut by queue, owner, source and hour
of arrival, with the count in every cut, and the pattern says what the
evidence does not support saying. Every figure names the query it came
from, and the period is kept so the numbers replay. A run is never
closed and reopened to shorten its elapsed time, and a moved item that
is already past its clock is recorded as a miss against its first
arrival with the misroute as its reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
