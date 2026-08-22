---
name: set-what-each-clock-covers
description: Takes the promise and the window being measured, and writes down what starts each clock, what stops it and what pauses it, so that two people read it the same way. Use it when running `ref/rev/watch-the-response-clock` and `ref/rev/write-a-routing-rule`.
license: CC-BY-4.0
metadata:
  agent: response-clock-monitor
  agent-version: "1"
---

# Set what each clock covers

## What it does

Takes the promise and the window being measured, and writes down what
starts each clock, what stops it and what pauses it, so that two people
read it the same way. Where a new rule promises a clock, that promise is
written the same way before the rule runs.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Name What Each Clock Covers**
  - `ref/rev/watch-the-response-clock`, activity 2 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)
- **Set the Clock the Rule Promises**
  - `ref/rev/write-a-routing-rule`, activity 8 -
    [Write a Routing Rule](../../../../processes/revenue-operations/write-a-routing-rule.md)
- **Take in the Promise and the Window**
  - `ref/rev/watch-the-response-clock`, activity 1 -
    [Watch the Response Clock](../../../../processes/revenue-operations/watch-the-response-clock.md)

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
