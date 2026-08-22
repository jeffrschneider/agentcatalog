---
name: score-material-against-the-rules
description: The agent reads a piece against the rules that apply to it and gives every item a verdict that cites the rule and the market it comes from. Use it when running `ref/mkt/approve-marketing-material` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: disclosure-check
  agent-version: "1"
---

# Score material against the rules

## What it does

The agent reads a piece against the rules that apply to it and gives
every item a verdict that cites the rule and the market it comes from.
It scores a draft before it runs and it scores the sized or adapted
versions again.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Check the Comparisons**
  - `ref/mkt/competitive-battlecard`, activity 11 -
    [Refresh Competitive Battlecard](../../../../processes/marketing/competitive-battlecard.md)
- **Review the Drafts**
  - `ref/mkt/influencer-campaign`, activity 12 -
    [Run Influencer Campaign](../../../../processes/marketing/influencer-campaign.md)
- **Score against the Disclosure Rules**
  - `ref/mkt/approve-marketing-material`, activity 5 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Score the Adapted Set**
  - `ref/mkt/traffic-ad-creative`, activity 7 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

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
