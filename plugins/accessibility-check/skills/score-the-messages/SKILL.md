---
name: score-the-messages
description: Brand, claims, rendering and accessibility checked. Use it when running `ref/mkt/nurture-sequence` and `ref/mkt/win-back-campaign`.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Score the Messages

## What happens

Brand, claims, rendering and accessibility checked.

## Where it happens

- `ref/mkt/nurture-sequence`, activity 9 -
  [Build Nurture Sequence](../../../../processes/marketing/nurture-sequence.md)
- `ref/mkt/win-back-campaign`, activity 10 -
  [Run Win-Back Campaign](../../../../processes/marketing/win-back-campaign.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
