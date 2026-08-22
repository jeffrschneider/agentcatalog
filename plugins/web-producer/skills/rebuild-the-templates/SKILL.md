---
name: rebuild-the-templates
description: Remakes the templates the rest of the material is built from, so that everything produced after them comes out right. Use it when running `ref/mkt/brand-refresh`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Rebuild the templates

## What it does

Remakes the templates the rest of the material is built from, so that
everything produced after them comes out right.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Rebuild the Templates**
  - `ref/mkt/brand-refresh`, activity 12 -
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
