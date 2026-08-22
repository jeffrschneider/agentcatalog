---
name: set-the-addresses-and-the-redirects
description: Sets the address a page lives at and points merged and retired pages somewhere sensible. Use it when running `ref/mkt/refresh-content`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Set the addresses and the redirects

## What it does

Sets the address a page lives at and points merged and retired pages
somewhere sensible.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Set the Addresses and the Redirects**
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
