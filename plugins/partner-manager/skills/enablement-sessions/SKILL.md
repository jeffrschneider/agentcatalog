---
name: enablement-sessions
description: Runs the live sessions that train a partner, records them for whoever could not attend, and answers and files the questions that come back afterwards. Use it when running `ref/mkt/enable-channel-partner`.
license: CC-BY-4.0
metadata:
  agent: partner-manager
  agent-version: "1"
---

# Enablement sessions

## What it does

Runs the live sessions that train a partner, records them for whoever
could not attend, and answers and files the questions that come back
afterwards.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Answer the Partner's Questions**
  - `ref/mkt/enable-channel-partner`, activity 11 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)
- **Run the Session**
  - `ref/mkt/enable-channel-partner`, activity 10 -
    [Enable Channel Partner](../../../../processes/marketing/enable-channel-partner.md)

## What to record

The partner record at a version, naming the agreement it rests on, the
tier the partner holds, the date that tier was set and who set it. For
everything the partner was given, the version it was at and the date it
went to them. For every person the partner put through training, what
they were trained on and the date they finished. A dated line for each
obligation as it comes due, saying whether it was met and by whom. What
the partner delivered back, counted against what the agreement asked
for, at the cadence the process sets. The CONVENED and DONE records of
everything it convenes, and the approval record behind every release and
every tier change.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
