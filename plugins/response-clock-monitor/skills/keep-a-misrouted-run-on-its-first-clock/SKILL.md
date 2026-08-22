---
name: keep-a-misrouted-run-on-its-first-clock
description: Holds the clock where it is when work moves because it reached the wrong person, so the run stays measured from when it first arrived. Use it when running `ref/rev/fix-a-misroute`.
license: CC-BY-4.0
metadata:
  agent: response-clock-monitor
  agent-version: "1"
---

# Keep a misrouted run on its first clock

## What it does

Holds the clock where it is when work moves because it reached the wrong
person, so the run stays measured from when it first arrived. The time
that misroute cost is filed against the rule version that produced it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **File the Case Against the Rule**
  - `ref/rev/fix-a-misroute`, activity 14 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)
- **Hold the Clock Where It Is**
  - `ref/rev/fix-a-misroute`, activity 3 -
    [Fix a Misroute](../../../../processes/revenue-operations/fix-a-misroute.md)

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
