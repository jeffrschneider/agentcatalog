---
name: send-the-touches
description: Prepares the sending, then works the cadence across mail, phone and social on the day each touch is due, inside the cap each channel sets. Use it when running `ref/sls/run-an-outbound-sequence`.
license: CC-BY-4.0
metadata:
  agent: sequence-operator
  agent-version: "1"
---

# Send the touches

## What it does

Prepares the sending, then works the cadence across mail, phone and
social on the day each touch is due, inside the cap each channel sets.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Make the Calls**
  - `ref/sls/run-an-outbound-sequence`, activity 9 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Prepare the Sending**
  - `ref/sls/run-an-outbound-sequence`, activity 7 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Run the Social Touches**
  - `ref/sls/run-an-outbound-sequence`, activity 10 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Send the First Touch**
  - `ref/sls/run-an-outbound-sequence`, activity 8 -
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
