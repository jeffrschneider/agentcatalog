---
name: score-against-the-disclosure-rules
description: The disclosures and disclaimers the piece must carry. Use it when running `ref/mkt/approve-marketing-material`.
license: CC-BY-4.0
metadata:
  agent: disclosure-check
  agent-version: "1"
---

# Score against the Disclosure Rules

## What happens

The disclosures and disclaimers the piece must carry.

## Where it happens

- `ref/mkt/approve-marketing-material`, activity 5 -
  [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)

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
