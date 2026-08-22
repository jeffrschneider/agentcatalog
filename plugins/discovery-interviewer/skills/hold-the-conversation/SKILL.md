---
name: hold-the-conversation
description: Runs the call to the question set, and follows the answers when the buyer opens ground the questions did not plan for. Use it when running `ref/sls/record-the-requirements` and `ref/sls/run-a-discovery-call`.
license: CC-BY-4.0
metadata:
  agent: discovery-interviewer
  agent-version: "1"
---

# Hold the conversation

## What it does

Runs the call to the question set, and follows the answers when the
buyer opens ground the questions did not plan for. Goes back to the
buyer afterwards with the questions a later reading of the notes raised.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Ask the Follow-Up Questions**
  - `ref/sls/record-the-requirements`, activity 6 -
    [Record the Requirements](../../../../processes/sales/record-the-requirements.md)
- **Follow the Answers**
  - `ref/sls/run-a-discovery-call`, activity 8 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Hold the Call**
  - `ref/sls/run-a-discovery-call`, activity 7 -
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
