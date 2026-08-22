---
name: read-the-market-rules
description: The agent gathers the disclosure rules in force in every market a piece will run in, at the version the organization has adopted, and writes down what each one requires. Use it when running `ref/mkt/influencer-campaign`.
license: CC-BY-4.0
metadata:
  agent: disclosure-check
  agent-version: "1"
---

# Read the market rules

## What it does

The agent gathers the disclosure rules in force in every market a piece
will run in, at the version the organization has adopted, and writes
down what each one requires.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Read the Disclosure Rules**
  - `ref/mkt/influencer-campaign`, activity 3 -
    [Run Influencer Campaign](../../../../processes/marketing/influencer-campaign.md)

## What to record

A verdict per item, each citing the rule, its version, the market it
applies in, and the version of the material it was read against. The
market and channel list the piece was scored against, recorded with the
score, so a later run into a new market is scored again. Where a rule
requires particular wording, the wording it requires, recorded beside
the item. A market the organization holds no rules for is recorded as
unscored. A rescore after a fix names what changed and what it ran
again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
