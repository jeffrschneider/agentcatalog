---
name: check-the-setup
description: Each version serves and its numbers arrive. Use it when running `ref/mkt/conversion-experiment`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Check the Setup

## What happens

Each version serves and its numbers arrive.

## Where it happens

- `ref/mkt/conversion-experiment`, activity 10 -
  [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
