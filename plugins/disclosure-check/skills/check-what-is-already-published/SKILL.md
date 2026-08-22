---
name: check-what-is-already-published
description: The agent reads material that is already live and reports anything running without the disclosure its market requires. Use it when running `ref/mkt/influencer-campaign`.
license: CC-BY-4.0
metadata:
  agent: disclosure-check
  agent-version: "1"
---

# Check what is already published

## What it does

The agent reads material that is already live and reports anything
running without the disclosure its market requires.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check the Disclosure**
  - `ref/mkt/influencer-campaign`, activity 15 -
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
