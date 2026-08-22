---
name: say-what-the-call-did-not-answer
description: Lists what the call did not answer, each with what it would change, and says whether one more conversation is needed or there is enough to shape against. Use it when running `ref/sls/run-a-discovery-call`.
license: CC-BY-4.0
metadata:
  agent: discovery-interviewer
  agent-version: "1"
---

# Say what the call did not answer

## What it does

Lists what the call did not answer, each with what it would change, and
says whether one more conversation is needed or there is enough to shape
against.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Decide If Another Call Is Needed**
  - `ref/sls/run-a-discovery-call`, activity 12 -
    [Run a Discovery Call](../../../../processes/sales/run-a-discovery-call.md)
- **Write Down What Is Not Known**
  - `ref/sls/run-a-discovery-call`, activity 11 -
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
