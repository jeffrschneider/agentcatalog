---
name: issue-the-release
description: The release is sent and the page on the site goes live. Use it when running `ref/mkt/announce-company-news`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Issue the Release

## What happens

The release is sent and the page on the site goes live.

## Where it happens

- `ref/mkt/announce-company-news`, activity 12 -
  [Announce Company News](../../../../processes/marketing/announce-company-news.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
