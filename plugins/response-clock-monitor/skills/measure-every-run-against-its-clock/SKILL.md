---
name: measure-every-run-against-its-clock
description: Checks first that the stamps hold up, such as missing stops and back-dated stamps, then marks every run or case in the window met, missed, or still open past its due time, with its start, its stop, its queue and its owner. Use it when running `ref/rev/watch-the-response-clock`, `ref/sup/report-the-service-levels` and `ref/sup/set-a-service-level-policy`.
license: CC-BY-4.0
metadata:
  agent: response-clock-monitor
  agent-version: "1"
---

# Measure every run against its clock

## What it does

Checks first that the stamps hold up, such as missing stops and
back-dated stamps, then marks every run or case in the window met,
missed, or still open past its due time, with its start, its stop, its
queue and its owner. Runs the clock never fitted are set aside with a
written reason and the name of the person who agreed, and the set-aside
count is published beside the result. The same reading runs over the
last periods against the levels in force, and from the day new levels
take effect.

## Where it happens

The agent does this in six activities across three reference processes.
Each one names the activity as that process words it.

- **Check the Stamps Hold Up**
  - `ref/sup/report-the-service-levels`, activity 3 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Measure Each Case Against Its Clock**
  - `ref/sup/report-the-service-levels`, activity 5 -
    [Report the Service Levels](../../../../processes/customer-support/report-the-service-levels.md)
- **Measure Each Run Against Its Clock**
  - `ref/rev/watch-the-response-clock`, activity 6 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
- **Measure from the Day It Takes Effect**
  - `ref/sup/set-a-service-level-policy`, activity 18 -
    [Set a Service Level Policy](../../../../processes/customer-support/set-a-service-level-policy.md)
- **Read the Results Against Today's Levels**
  - `ref/sup/set-a-service-level-policy`, activity 4 -
    [Set a Service Level Policy](../../../../processes/customer-support/set-a-service-level-policy.md)
- **Set Aside What the Clock Does Not Cover**
  - `ref/rev/watch-the-response-clock`, activity 7 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
  - `ref/sup/report-the-service-levels`, activity 6 -
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
