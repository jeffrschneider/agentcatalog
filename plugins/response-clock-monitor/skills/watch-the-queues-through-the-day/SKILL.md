---
name: watch-the-queues-through-the-day
description: Watches each queue's waiting cases against their clocks through the day, names a queue about to miss with the cases at risk and the time each has left, and checks the queue recovers once a person has changed something. Use it when running `ref/sup/run-the-days-queue`.
license: CC-BY-4.0
metadata:
  agent: response-clock-monitor
  agent-version: "1"
---

# Watch the queues through the day

## What it does

Watches each queue's waiting cases against their clocks through the day,
names a queue about to miss with the cases at risk and the time each has
left, and checks the queue recovers once a person has changed something.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check the Queue Recovers**
  - `ref/sup/run-the-days-queue`, activity 13 -
    [Run the Day's Queue](../../../../processes/customer-support/run-the-days-queue.md)
- **Name a Queue About to Miss**
  - `ref/sup/run-the-days-queue`, activity 7 -
    [Run the Day's Queue](../../../../processes/customer-support/run-the-days-queue.md)
- **Watch Each Queue Against Its Clock**
  - `ref/sup/run-the-days-queue`, activity 3 -
    [Run the Day's Queue](../../../../processes/customer-support/run-the-days-queue.md)

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
