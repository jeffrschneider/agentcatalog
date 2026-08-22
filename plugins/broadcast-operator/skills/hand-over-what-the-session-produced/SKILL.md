---
name: hand-over-what-the-session-produced
description: Passes on everything the session produced once it ends, which is the recording, the attendance record, the poll answers and every question that was asked. Use it when running `ref/mkt/webinar`.
license: CC-BY-4.0
metadata:
  agent: broadcast-operator
  agent-version: "1"
---

# Hand over what the session produced

## What it does

Passes on everything the session produced once it ends, which is the
recording, the attendance record, the poll answers and every question
that was asked.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Hand over What the Session Produced**
  - `ref/mkt/webinar`, activity 13 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)

## What to record

The session as it was set up, at a version, saying the date, the time,
who may join and how, what material was loaded, and which polls were
prepared. The rehearsal record, saying which presenters connected, which
were heard, which shared successfully, what failed, and what was still
unresolved when the rehearsal ended. A dated record of the live session,
saying when it started, when it ended, who was on air at each point,
when each poll opened and closed, and anything that went wrong with the
time it happened. The recording at a version. The attendance record,
naming who registered, who joined, when each person joined and left, and
how long they stayed. The poll answers as the platform recorded them.
Every question that was asked, with the time it came in, whether it was
answered on air, and which questions were still unanswered when the
session ended.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
