---
name: see-a-settled-carve-land-once
description: Confirms that what goes into the systems and out to the field is the version that was checked, and that an account moves in one place rather than in several. Use it when running `ref/rev/move-an-account` and `ref/rev/publish-the-carve`.
license: CC-BY-4.0
metadata:
  agent: coverage-check
  agent-version: "1"
---

# See a settled carve land once

## What it does

Confirms that what goes into the systems and out to the field is the
version that was checked, and that an account moves in one place rather
than in several. Nothing publishes while a hole is still open.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Change the Systems Once**
  - `ref/rev/move-an-account`, activity 10 -
    [Move an Account](../../../../processes/revenue-operations/move-an-account.md)
- **Publish the Final Carve**
  - `ref/rev/publish-the-carve`, activity 13 -
    [Publish the Carve](../../../../processes/revenue-operations/publish-the-carve.md)

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
