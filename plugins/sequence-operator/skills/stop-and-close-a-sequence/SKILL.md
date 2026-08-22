---
name: stop-and-close-a-sequence
description: Stops the touches the moment a meeting is confirmed, and does not start them again. Use it when running `ref/sls/book-the-meeting` and `ref/sls/run-an-outbound-sequence`.
license: CC-BY-4.0
metadata:
  agent: sequence-operator
  agent-version: "1"
---

# Stop and close a sequence

## What it does

Stops the touches the moment a meeting is confirmed, and does not start
them again. Closes the sequence at the end, cancels the touches still
scheduled, and reports what was sent, what came back and what the run
taught.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Close the Sequence**
  - `ref/sls/run-an-outbound-sequence`, activity 16 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Report and Record What Was Learned**
  - `ref/sls/run-an-outbound-sequence`, activity 17 -
    [Run an Outbound Sequence](../../../../processes/sales/run-an-outbound-sequence.md)
- **Stop the Outbound Touches**
  - `ref/sls/book-the-meeting`, activity 14 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)

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
