---
name: repurpose-existing-material
description: Turns material that already exists into new pages and pieces, which includes cutting a recording, adding captions and building the page it sits on. Use it when running `ref/mkt/user-conference` and `ref/mkt/webinar`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Repurpose existing material

## What it does

Turns material that already exists into new pages and pieces, which
includes cutting a recording, adding captions and building the page it
sits on.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Prepare the Recording for Reuse**
  - `ref/mkt/webinar`, activity 14 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)
- **Repurpose the Content**
  - `ref/mkt/user-conference`, activity 15 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)

## What to record

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
