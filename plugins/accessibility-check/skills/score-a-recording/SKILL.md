---
name: score-a-recording
description: Scores a recording and the things published with it, which means the captions, the cut, and the page the recording sits on. Use it when running `ref/mkt/webinar`.
license: CC-BY-4.0
metadata:
  agent: accessibility-check
  agent-version: "1"
---

# Score a recording

## What it does

Scores a recording and the things published with it, which means the
captions, the cut, and the page the recording sits on.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Prepare the Recording for Reuse**
  - `ref/mkt/webinar`, activity 14 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)

## What to record

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
