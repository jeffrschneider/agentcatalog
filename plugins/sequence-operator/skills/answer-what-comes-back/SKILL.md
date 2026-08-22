---
name: answer-what-comes-back
description: Reads every reply the same day and sorts it into wants a conversation, not now, wrong person or stop. Use it when running `ref/sls/run-an-outbound-sequence`.
license: CC-BY-4.0
metadata:
  agent: sequence-operator
  agent-version: "1"
---

# Answer what comes back

## What it does

Reads every reply the same day and sorts it into wants a conversation,
not now, wrong person or stop. A reply stops the sequence on every
channel before the next scheduled send, and a stop suppresses the person
everywhere and not only where they said it. A reply that wants a
conversation goes on with the whole thread attached.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Hand over the Positive Replies**
  - `ref/sls/run-an-outbound-sequence`, activity 15 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Handle Opt-Outs**
  - `ref/sls/run-an-outbound-sequence`, activity 13 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Stop on a Reply**
  - `ref/sls/run-an-outbound-sequence`, activity 12 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Watch for Replies**
  - `ref/sls/run-an-outbound-sequence`, activity 11 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)

## What to record

The cadence and the wording as signed, at a version, with the signer and
the date, and any change after signing recorded as voiding that
signature. Per person: every touch sent, on which channel and on which
day, what the call notes say, the reply as it arrived and how it was
sorted into wants a conversation, not now, wrong person or stop, the
time the stop took effect, and the words behind any opt-out. Per run:
the bounces, complaints and blocks read against the sending thresholds,
every send held back and why, the people who reached the end of the
cadence without answering, and the touches cancelled when the sequence
closed.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
