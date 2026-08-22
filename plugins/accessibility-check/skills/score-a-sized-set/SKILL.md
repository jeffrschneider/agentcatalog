---
name: score-a-sized-set
description: Scores every version in a set that was resized or adapted for a different placement, because a version that passes at one size can fail at another. Use it when running `ref/mkt/creative-assets` and `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Score a sized set

## What it does

Scores every version in a set that was resized or adapted for a
different placement, because a version that passes at one size can fail
at another.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Sized Set**
  - `ref/mkt/creative-assets`, activity 11 -
    [Produce Creative Assets](../../../../processes/marketing/creative-assets.md)
- **Score the Adapted Set**
  - `ref/mkt/traffic-ad-creative`, activity 7 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
