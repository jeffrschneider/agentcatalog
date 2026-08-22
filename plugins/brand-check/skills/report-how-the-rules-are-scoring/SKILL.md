---
name: report-how-the-rules-are-scoring
description: The agent reads the scoring record over time and reports which rules keep failing and which ones nobody ever applies. Use it when running `ref/mkt/brand-voice`.
license: CC-BY-4.0
metadata:
  agent: brand-check
  agent-version: "1"
---

# Report how the rules are scoring

## What it does

The agent reads the scoring record over time and reports which rules
keep failing and which ones nobody ever applies.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Watch How the Rules Score**
  - `ref/mkt/brand-voice`, activity 18 -
    [Define Brand Voice and Messaging](../../../../processes/marketing/brand-voice.md)

## What to record

A score per item, each citing the standard, its version, and the rule
applied. What passed, what failed, and why, in a form the human signers
read in minutes.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
