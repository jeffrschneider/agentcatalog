---
name: break-the-misses-down
description: Cuts the misses by queue, owner, source and hour of arrival, with the count in every cut, and for the support desk by queue, channel, topic, plan and hour with no named person in any cut. Use it when running `ref/rev/watch-the-response-clock`, `ref/sup/build-the-support-schedule` and `ref/sup/report-the-service-levels`.
license: CC-BY-4.0
metadata:
  agent: response-clock-monitor
  agent-version: "1"
---

# Break the misses down

## What it does

Cuts the misses by queue, owner, source and hour of arrival, with the
count in every cut, and for the support desk by queue, channel, topic,
plan and hour with no named person in any cut. Says what the misses have
in common only as far as the evidence supports saying it.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Break the Misses Down**
  - `ref/rev/watch-the-response-clock`, activity 8 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
  - `ref/sup/report-the-service-levels`, activity 7 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Find What the Misses Have in Common**
  - `ref/rev/watch-the-response-clock`, activity 9 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
- **Find the Cause Behind the Misses**
  - `ref/sup/report-the-service-levels`, activity 8 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Read Where the Last Schedule Missed**
  - `ref/sup/build-the-support-schedule`, activity 5 -
    [Build the Support Schedule](../../../../processes/customer-support/build-the-support-schedule.md)

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
