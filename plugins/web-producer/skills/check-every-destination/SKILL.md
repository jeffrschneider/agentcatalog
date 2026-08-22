---
name: check-every-destination
description: The page each ad points at loads and records the visit. Use it when running `ref/mkt/traffic-ad-creative`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Check Every Destination

## What happens

The page each ad points at loads and records the visit.

## Where it happens

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
