---
name: score-a-design-system
description: Scores the parts of a visual system before anything is built from it, which means the palette against the contrast rules and the type against the legibility rules. Use it when running `ref/mkt/brand-guidelines` and `ref/mkt/brand-identity`.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Score a design system

## What it does

Scores the parts of a visual system before anything is built from it,
which means the palette against the contrast rules and the type against
the legibility rules. It also scores a page and a deck built from that
system, so a rule that only fails in use is caught.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Colors and the Type**
  - `ref/mkt/brand-guidelines`, activity 9 -
    [Publish Brand Guidelines](../../../../processes/marketing/brand-guidelines.md)
- **Test the System in Use**
  - `ref/mkt/brand-identity`, activity 12 -
    [Develop Brand Identity](../../../../processes/marketing/brand-identity.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
