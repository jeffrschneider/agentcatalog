---
name: capture-what-was-said-and-confirm-it
description: Captures the notes in the buyer's own words, with a speaker against each line and any paraphrase marked as a paraphrase, then reads the summary back for confirmation. Use it when running `ref/sls/run-a-discovery-call`.
license: CC-BY-4.0
metadata:
  agent: discovery-interviewer
  agent-version: "1"
---

# Capture what was said and confirm it

## What it does

Captures the notes in the buyer's own words, with a speaker against each
line and any paraphrase marked as a paraphrase, then reads the summary
back for confirmation. Silence on the read-back is not confirmation.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Capture What Was Said**
  - `ref/sls/run-a-discovery-call`, activity 9 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Read the Summary Back**
  - `ref/sls/run-a-discovery-call`, activity 10 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)

## What to record

What the call has to settle, for whom, and by when. The people asked for
and the people who came. The question set at a version, with the
questions that must not be left unasked marked as such, and the ones
that were dropped noted. The buyer's written consent to record and where
the recording is kept, or the record that consent was refused and the
call went ahead unrecorded. The notes in the words the buyer used, with
the speaker against each line and any paraphrase marked as a paraphrase.
The read-back, and the buyer's confirmation or corrections. The
questions the call did not answer, each with what it would change. The
retention date the notes and the recording are held to.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
