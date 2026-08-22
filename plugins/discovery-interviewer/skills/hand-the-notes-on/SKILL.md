---
name: hand-the-notes-on
description: Hands the confirmed notes to whoever writes the requirement record, and records what the call taught about the questions asked and the people who came. Use it when running `ref/sls/run-a-discovery-call`.
license: CC-BY-4.0
metadata:
  agent: discovery-interviewer
  agent-version: "1"
---

# Hand the notes on

## What it does

Hands the confirmed notes to whoever writes the requirement record, and
records what the call taught about the questions asked and the people
who came.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Hand the Notes On**
  - `ref/sls/run-a-discovery-call`, activity 13 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Record What the Call Taught**
  - `ref/sls/run-a-discovery-call`, activity 14 -
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
