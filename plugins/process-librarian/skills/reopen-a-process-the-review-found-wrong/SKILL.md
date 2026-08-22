---
name: reopen-a-process-the-review-found-wrong
description: Reads the reasons people gave for departing and says whether the process is wrong or the process is ignored, then opens the amendments for the steps that were wrong so they are documented again. Use it when running `ref/rev/review-adoption`.
license: CC-BY-4.0
metadata:
  agent: process-librarian
  agent-version: "1"
---

# Reopen a process the review found wrong

## What it does

Reads the reasons people gave for departing and says whether the process
is wrong or the process is ignored, then opens the amendments for the
steps that were wrong so they are documented again.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Open the Process Amendments**
  - `ref/rev/review-adoption`, activity 13 -
    [Review Adoption](../../../../processes/revenue-operations/review-adoption.md)
- **Sort the Reasons**
  - `ref/rev/review-adoption`, activity 6 -
    [Review Adoption](../../../../processes/revenue-operations/review-adoption.md)

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
