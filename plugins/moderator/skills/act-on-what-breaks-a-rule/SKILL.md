---
name: act-on-what-breaks-a-rule
description: Carries out the action a verdict calls for on the community platform, which can be hiding a post, removing it, or restricting what a member may do. Use it when running `ref/mkt/moderate-community`.
license: CC-BY-4.0
metadata:
  agent: moderator
  agent-version: "1"
---

# Act on what breaks a rule

## What it does

Carries out the action a verdict calls for on the community platform,
which can be hiding a post, removing it, or restricting what a member
may do. It records the rule the action was taken under and tells the
member what happened and how to put it in front of a person.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Remove What Breaks the Rules**
  - `ref/mkt/moderate-community`, activity 8 -
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
