---
name: look-for-candidates
description: Looks for companies that could close the gap. Use it when running `ref/prt/find-a-partner`.
license: CC-BY-4.0
metadata:
  agent: partner-scout
  agent-version: "1"
---

# Look for candidates

## What it does

Looks for companies that could close the gap. Reads the partners,
customers and suppliers already on the books first and goes out to the
market only after that, so a partner we already have is not missed in
favour of a new name.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Look at Who We Already Know**
  - `ref/prt/find-a-partner`, activity 6 -
    [Find a Partner](../../../../processes/partners/find-a-partner.md)
- **Search the Market**
  - `ref/prt/find-a-partner`, activity 7 -
    [Find a Partner](../../../../processes/partners/find-a-partner.md)

## What to record

The search bounds it was given, including the companies it may not
touch. Every candidate with the source it came from and the date it was
read. Every removal with the reason it was removed. Every score against
the closing test with the evidence line behind it and the date that
evidence was read, so a second person scoring the same candidate can get
the same answer or say where they differ. The approach as sent, the
date, and what each candidate was told. The replies, the refusals and
the silences, each dated.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
