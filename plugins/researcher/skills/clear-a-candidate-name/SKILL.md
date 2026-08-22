---
name: clear-a-candidate-name
description: Checks a candidate name before anybody commits to it. Use it when running `ref/mkt/brand-identity` and `ref/mkt/name-product`.
license: CC-BY-4.0
metadata:
  agent: researcher
  agent-version: "1"
---

# Clear a candidate name

## What it does

Checks a candidate name before anybody commits to it. It searches the
registers for marks already in use, and finds out what the name means
and how it sounds in every market where it will be used.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Name in Every Market**
  - `ref/mkt/name-product`, activity 7 -
    [Name Product or Company](../../../../processes/marketing/name-product.md)
- **Clear the Candidate Marks**
  - `ref/mkt/brand-identity`, activity 8 -
    [Develop Brand Identity](../../../../processes/marketing/brand-identity.md)

## What to record

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
