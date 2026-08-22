---
name: score-the-adapted-set
description: The sized set read against the standards and the rules. Use it when running `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: disclosure-check
  agent-version: "1"
---

# Score the Adapted Set

## What happens

The sized set read against the standards and the rules.

## Where it happens

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
