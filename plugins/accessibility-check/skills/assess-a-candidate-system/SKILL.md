---
name: assess-a-candidate-system
description: Reads what a system under consideration produces and says whether that output can meet the standards in force, before anybody commits to it. Use it when running `ref/mkt/select-marketing-technology`.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Assess a candidate system

## What it does

Reads what a system under consideration produces and says whether that
output can meet the standards in force, before anybody commits to it.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Check It against the Standards**
  - `ref/mkt/select-marketing-technology`, activity 13 -
    [Select Marketing Technology](../../../../processes/marketing/select-marketing-technology.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
