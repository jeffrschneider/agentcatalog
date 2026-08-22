---
name: write-rules-that-can-be-scored
description: The agent turns a standard into numbered rules written tightly enough that a scoring agent can apply them, each one with a passing and a failing example. Use it when running `ref/mkt/brand-guidelines` and `ref/mkt/brand-voice`.
license: CC-BY-4.0
metadata:
  agent: editor
  agent-version: "1"
---

# Write rules that can be scored

## What it does

The agent turns a standard into numbered rules written tightly enough
that a scoring agent can apply them, each one with a passing and a
failing example.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Turn the Voice into Scorable Rules**
  - `ref/mkt/brand-voice`, activity 11 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)
- **Write the Rules**
  - `ref/mkt/brand-guidelines`, activity 5 -
    [Publish Brand Guidelines](../../../../processes/marketing/brand-guidelines.md)

## What to record

Every edit at a version, saying what has to change and why, item by
item, in terms the writer can work through without coming back to ask
what was meant. A line for anything it flagged for another pass, naming
the agent it went to. When it holds the version, the merge, the decline
or the revision request it gave in every round, each with its reason.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
