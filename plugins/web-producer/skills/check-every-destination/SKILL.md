---
name: check-every-destination
description: Opens the page behind every live link and confirms that it loads and that the visit is recorded. Use it when running `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Check every destination

## What it does

Opens the page behind every live link and confirms that it loads and
that the visit is recorded.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check Every Destination**
  - `ref/mkt/traffic-ad-creative`, activity 10 -
    [Traffic Ad Creative](../../../../processes/marketing/traffic-ad-creative.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
