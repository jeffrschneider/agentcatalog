---
name: prepare-a-discovery-call
description: Works out what the call has to settle, for whom and by when, reads the account first, and names who has to be in the room. Use it when running `ref/sls/run-a-discovery-call`.
license: CC-BY-4.0
metadata:
  agent: discovery-interviewer
  agent-version: "1"
---

# Prepare a discovery call

## What it does

Works out what the call has to settle, for whom and by when, reads the
account first, and names who has to be in the room. Writes the question
set in the order that covers the ground, and gets the recording agreed
in writing before anything is captured.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Agree How the Call Is Recorded**
  - `ref/sls/run-a-discovery-call`, activity 6 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Decide Who Should Be in the Room**
  - `ref/sls/run-a-discovery-call`, activity 3 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Read the Account First**
  - `ref/sls/run-a-discovery-call`, activity 2 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Take in the Opportunity**
  - `ref/sls/run-a-discovery-call`, activity 1 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Write the Question Set**
  - `ref/sls/run-a-discovery-call`, activity 5 -
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
