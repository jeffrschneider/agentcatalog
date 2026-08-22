---
name: score-finished-material
description: Scores a finished piece of material against the accessibility and technical standards it was handed, at the versions those standards were named at, and reports what passed, what failed and what could not be tested. Use it when running `ref/mkt/approve-marketing-material` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Score finished material

## What it does

Scores a finished piece of material against the accessibility and
technical standards it was handed, at the versions those standards were
named at, and reports what passed, what failed and what could not be
tested.

## Where it happens

The agent does this in three activities across four reference processes.
Each one names the activity as that process words it.

- **Check the Remade Material**
  - `ref/mkt/brand-refresh`, activity 17 -
    [Roll Out Brand Refresh](../../../../processes/marketing/brand-refresh.md)
- **Score against the Accessibility Rules**
  - `ref/mkt/approve-marketing-material`, activity 6 -
    [Approve Marketing Material](../../../../processes/marketing/approve-marketing-material.md)
- **Score against the Standards**
  - `ref/mkt/creative-assets`, activity 8 -
    [Produce Creative Assets](../../../../processes/marketing/creative-assets.md)
  - `ref/mkt/video-asset`, activity 11 -
    [Produce Video Asset](../../../../processes/marketing/video-asset.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
