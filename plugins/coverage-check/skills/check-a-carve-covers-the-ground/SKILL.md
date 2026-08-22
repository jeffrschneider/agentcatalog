---
name: check-a-carve-covers-the-ground
description: Reads the account base against the map and names what nobody owns, what sits in two patches, what is too big for the seller behind it and what is too small to live on. Use it when running `ref/rev/model-the-territories` and `ref/rev/publish-the-carve`.
license: CC-BY-4.0
metadata:
  agent: coverage-check
  agent-version: "1"
---

# Check a carve covers the ground

## What it does

Reads the account base against the map and names what nobody owns, what
sits in two patches, what is too big for the seller behind it and what
is too small to live on. Reads a finished period the same way, naming
the patches that were worked, the ones nobody ever called, and the
accounts left with no owner at all.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check Coverage and Balance**
  - `ref/rev/model-the-territories`, activity 10 -
    [Model the Territories](../../../../processes/revenue-operations/model-the-territories.md)
- **Check the Carve Is Whole**
  - `ref/rev/publish-the-carve`, activity 2 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)
- **Read How Last Year Was Covered**
  - `ref/rev/model-the-territories`, activity 6 -
    [Model the Territories](../../../../processes/revenue-operations/model-the-territories.md)

## What to record

Per check: every account in no patch and every account in two, named
rather than counted; every patch nobody holds and every seller holding
more than one; every patch over the stated account count or amount and
every patch under the floor, each failure naming the rule it failed.
Reading last period, it names which patches were worked, which were
never called, and what was left with no owner at all. Reading
statements, it names every place a page and the system that will pay on
it disagree, by seller. Reading a move, it quotes the line of the carve
that allows it as written, or records that no line covers it. Every
finding carries the version of the map and the quota set it was tested
against, so an auditor can rerun it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
