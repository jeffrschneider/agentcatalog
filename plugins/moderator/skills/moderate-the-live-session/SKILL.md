---
name: moderate-the-live-session
description: Sits in a session while it is on air, keeps it to the time it was given, and handles what the audience posts as it comes in. Use it when running `ref/mkt/webinar`.
license: CC-BY-4.0
metadata:
  agent: moderator
  agent-version: "1"
---

# Moderate the live session

## What it does

Sits in a session while it is on air, keeps it to the time it was given,
and handles what the audience posts as it comes in.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Run the Session**
  - `ref/mkt/webinar`, activity 12 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)

## What to record

Every action, with the post as it stood when it was read, the rule and
its version, the action taken, how long that action lasts, the time it
was taken, and the notice that went to the member. A post it read and
left alone is recorded where the process asks for that. An appeal is
recorded with the person's decision, and a reversal lands as a new
record while the original action stays where it is.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
