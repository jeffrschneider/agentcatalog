---
name: stage-changes-before-the-date
description: Builds and previews everything ahead of a date without any of it serving, so the people who have to look at it can, and so it all goes live together. Use it when running `ref/mkt/brand-refresh` and `ref/mkt/product-launch`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Stage changes before the date

## What it does

Builds and previews everything ahead of a date without any of it
serving, so the people who have to look at it can, and so it all goes
live together.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Prep the Channels**
  - `ref/mkt/product-launch`, activity 6 -
    [Launch Product](../../../../processes/marketing/product-launch.md)
- **Stage the Changes**
  - `ref/mkt/brand-refresh`, activity 18 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
