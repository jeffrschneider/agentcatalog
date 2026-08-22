---
name: open-registration
description: The registration page, with its tracking wired up. Use it when running `ref/mkt/field-event` and `ref/mkt/user-conference`.
license: CC-BY-4.0
metadata:
  agent: web-producer
  agent-version: "1"
---

# Open Registration

## What happens

The processes that use this activity word it differently:

- in `ref/mkt/field-event`, the registration page, with its tracking
  wired up
- in `ref/mkt/user-conference`, the site, the sign-up and the tracking
  go live

## Where it happens

- `ref/mkt/field-event`, activity 8 -
  [Host Field Event](../../../../processes/marketing/field-event.md)
- `ref/mkt/user-conference`, activity 7 -
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
