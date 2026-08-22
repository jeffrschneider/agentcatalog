---
name: deliver-the-score-into-a-sign-off
description: Puts its score in front of the people who sign, beside the other checks a version has to clear, and says plainly what is still outstanding. Use it when running `ref/mkt/conversion-experiment`.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Deliver the score into a sign off

## What it does

Puts its score in front of the people who sign, beside the other checks
a version has to clear, and says plainly what is still outstanding. It
does not sign anything itself.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Get Sign-Offs**
  - `ref/mkt/conversion-experiment`, activity 9 -
    [Run Conversion Experiment](../../../../processes/marketing/conversion-experiment.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
