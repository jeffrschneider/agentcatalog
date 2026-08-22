---
name: check-what-the-company-owed
description: Reads the other direction in a performance round, setting what the company promised each partner against what it actually delivered, and marking each difference settled or open. Use it when running `ref/prt/review-partner-performance`.
license: CC-BY-4.0
metadata:
  agent: margin-keeper
  agent-version: "1"
---

# Check what the company owed

## What it does

Reads the other direction in a performance round, setting what the
company promised each partner against what it actually delivered, and
marking each difference settled or open.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check What the Company Owed**
  - `ref/prt/review-partner-performance`, activity 6 -
    [Review Partner Performance](../../../../processes/partners/review-partner-performance.md)

## What to record

The priced tier table at a version, naming the rules version it was
priced against, the volume each tier assumes, and the margin, discount,
fund and support hours each one carries. The margin test per tier,
naming the floor it was set against and the shortfall where there is
one, with the name of whoever accepted a shortfall in writing. Per
partner, the discount in force and the date it started. Per system
changed, what it was set to and the date it took effect. For a
relationship ending, the settlement line by line: what was earned, what
was paid, what is recovered, and what is still open. For a performance
round, what the company owed each partner set against what was actually
delivered, with each difference settled or marked open.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
