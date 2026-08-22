---
name: open-a-run-and-fix-what-it-covers
description: Reads why a process is being written down now, and settles with the named owner where it starts, where it stops and who owns it. Use it when running `ref/rev/document-a-process`.
license: CC-BY-4.0
metadata:
  agent: process-librarian
  agent-version: "1"
---

# Open a run and fix what it covers

## What it does

Reads why a process is being written down now, and settles with the
named owner where it starts, where it stops and who owns it. Everything
the run watches afterwards sits inside those boundaries.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Name the Owner and the Boundaries**
  - `ref/rev/document-a-process`, activity 2 -
    [Document a Process](../../../../processes/revenue-operations/document-a-process.md)
- **Take in the Request**
  - `ref/rev/document-a-process`, activity 1 -
    [Document a Process](../../../../processes/revenue-operations/document-a-process.md)

## What to record

Per process: every existing description with its date, and the ones that
contradict each other paired up. What was observed, step by step, with
the steps nobody performed marked as unobserved. What people said,
attributed to a role rather than to a name. The activity walk, each step
carrying its doer, what starts it and what it hands on. The variants and
the thing each one turns on. Every disputed step with all its accounts
attached, and the reason recorded against each one the owner settled.
The standards check with the rule behind every failure. The signers by
name, with the date each one signed. The version, its address and the
list of documents it replaces. And what stayed vague, written down as
vague.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
