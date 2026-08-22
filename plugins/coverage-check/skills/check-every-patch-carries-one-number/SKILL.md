---
name: check-every-patch-carries-one-number
description: Sets the quota record against the map and names every patch that carries no number and every patch that carries two. Use it when running `ref/rev/set-the-quotas`.
license: CC-BY-4.0
metadata:
  agent: coverage-check
  agent-version: "1"
---

# Check every patch carries one number

## What it does

Sets the quota record against the map and names every patch that carries
no number and every patch that carries two. It runs before anything is
stated against those numbers.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check Every Patch Has One**
  - `ref/rev/set-the-quotas`, activity 10 -
    [Set the Quotas](../../../../processes/revenue-operations/set-the-quotas.md)

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
