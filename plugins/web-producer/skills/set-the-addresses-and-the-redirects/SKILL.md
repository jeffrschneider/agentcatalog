---
name: set-the-addresses-and-the-redirects
description: Merged and retired pages point somewhere sensible. Use it when running `ref/mkt/refresh-content`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Set the Addresses and the Redirects

## What happens

Merged and retired pages point somewhere sensible.

## Where it happens

- `ref/mkt/refresh-content`, activity 17 -
  [Refresh Published Content](../../../../processes/marketing/refresh-content.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
