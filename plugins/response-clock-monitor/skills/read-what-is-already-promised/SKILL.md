---
name: read-what-is-already-promised
description: Reads the levels each plan and agreement already promises customers, and checks each candidate level against them, naming every account a candidate would serve slower than its agreement promises. Use it when running `ref/sup/set-a-service-level-policy`.
license: CC-BY-4.0
metadata:
  agent: response-clock-monitor
  agent-version: "1"
---

# Read what is already promised

## What it does

Reads the levels each plan and agreement already promises customers, and
checks each candidate level against them, naming every account a
candidate would serve slower than its agreement promises.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check Each Against What Is Promised**
  - `ref/sup/set-a-service-level-policy`, activity 8 -
    [Set a Service Level Policy](../../../../processes/customer-support/set-a-service-level-policy.md)
- **Read What Customers Are Already Promised**
  - `ref/sup/set-a-service-level-policy`, activity 3 -
    [Set a Service Level Policy](../../../../processes/customer-support/set-a-service-level-policy.md)

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
