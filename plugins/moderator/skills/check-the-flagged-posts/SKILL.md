---
name: check-the-flagged-posts
description: Each one is scored against the rule it may break. Use it when running `ref/mkt/moderate-community`.
license: CC-BY-4.0
metadata:
  agent: moderator
  agent-version: "1"
---

# Check the Flagged Posts

## What happens

Each one is scored against the rule it may break.

## Where it happens

- `ref/mkt/moderate-community`, activity 7 -
  [Moderate User Community](../../../../processes/marketing/moderate-community.md)

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
