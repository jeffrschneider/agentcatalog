---
name: put-the-work-in-front-of-the-people-who-act
description: Puts the finished work in front of the people who decide and the agents that act on it, each option carrying its cost and what it rules out, and takes their reading of it before it issues. Use it when running `ref/mkt/analyze-customer-base` and `ref/mkt/plan-marketing-capacity`.
license: CC-BY-4.0
metadata:
  agent: forecaster
  agent-version: "1"
---

# Put the work in front of the people who act

## What it does

Puts the finished work in front of the people who decide and the agents
that act on it, each option carrying its cost and what it rules out, and
takes their reading of it before it issues.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Put the Options to the People Who Decide**
  - `ref/mkt/plan-marketing-capacity`, activity 10 -
    [Plan Marketing Capacity](../../../../processes/marketing/plan-marketing-capacity.md)
- **Review the Findings**
  - `ref/mkt/analyze-customer-base`, activity 15 -
    [Analyze Customer Base](../../../../processes/marketing/analyze-customer-base.md)

## What to record

Every model at a version, saying which data it was fit on, over what
period, and which records it left out and why. Every prediction with the
model version that produced it and the inputs it was computed from, so
somebody can run it again and see whether the answer still holds. Every
assumption written beside the number it drives, naming where the
assumption came from and how far the number moves when the assumption
moves. A back-test result whenever the agent says a profile would have
picked the right customers, showing what the profile would have selected
and what actually happened to those accounts. A list of every rate it
could not source, marked unsourced, carried into the report.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
