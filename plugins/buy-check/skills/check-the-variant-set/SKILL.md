---
name: check-the-variant-set
description: Each variant changes only the element under test. Use it when running `ref/mkt/test-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: buy-check
  agent-version: "1"
---

# Check the Variant Set

## What happens

Each variant changes only the element under test.

## Where it happens

- `ref/mkt/test-ad-creative`, activity 9 -
  [Test Ad Creative](../../../../processes/marketing/test-ad-creative.md)

## What to record

A verdict per item, each citing the plan line or the rule, its version,
and the campaign configuration it was read against. A pre-launch score
and a post-delivery score, each dated and each naming what it read.
Anything it could not test is recorded as untested rather than left out.
A rescore after a fix names what changed and what it ran again. Where
what ran differs from what was ordered, the difference is recorded
against the plan line it belongs to, with the figures on both sides.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
