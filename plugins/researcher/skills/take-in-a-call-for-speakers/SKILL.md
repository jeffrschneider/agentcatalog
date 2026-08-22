---
name: take-in-a-call-for-speakers
description: Reads a published call for speakers and works out what it is asking for, which is what the event is, who attends, and when it closes. Use it when running `ref/mkt/speaking-engagement`.
license: CC-BY-4.0
metadata:
  agent: researcher
  agent-version: "1"
---

# Take in a call for speakers

## What it does

Reads a published call for speakers and works out what it is asking for,
which is what the event is, who attends, and when it closes.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Take in the Call**
  - `ref/mkt/speaking-engagement`, activity 1 -
    [Secure Speaking Engagement](../../../../processes/marketing/speaking-engagement.md)

## What to record

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
