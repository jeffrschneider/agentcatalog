---
name: settle-what-a-rule-means
description: Answers a scoring agent that cannot tell from the text what a rule requires, and writes the answer down against the rule so everyone reading it afterwards gets the same answer. Use it when running `ref/mkt/approve-marketing-material`.
license: CC-BY-4.0
metadata:
  agent: standards-keeper
  agent-version: "1"
---

# Settle what a rule means

## What it does

Answers a scoring agent that cannot tell from the text what a rule
requires, and writes the answer down against the rule so everyone
reading it afterwards gets the same answer.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Settle a Disputed Rule**
  - `ref/mkt/approve-marketing-material`, activity 8 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)

## What to record

Every standard at a numbered version, with the date it took effect and
the date it stopped being current. A change record for each version,
saying what changed, what it replaced, who approved it, and when. Every
earlier version left readable at its own number, so work can be judged
against the standard it was made under. Every interpretation it issued,
attached to the rule and the version it interprets, carrying the
question that prompted it and the agent that asked. A dated record of
who was told about each change.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
