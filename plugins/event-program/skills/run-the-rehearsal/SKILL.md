---
name: run-the-rehearsal
description: Writes the minute-by-minute plan for the event and runs the rehearsal against it, so that every presenter has connected, used the equipment and run their part before an audience is there. Use it when running `ref/mkt/field-event` and `ref/mkt/webinar`.
license: CC-BY-4.0
metadata:
  agent: event-program
  agent-version: "1"
---

# Run the rehearsal

## What it does

Writes the minute-by-minute plan for the event and runs the rehearsal
against it, so that every presenter has connected, used the equipment
and run their part before an audience is there.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Prepare the Run of Show**
  - `ref/mkt/field-event`, activity 11 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Rehearse the Session**
  - `ref/mkt/webinar`, activity 11 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)

## What to record

The call for sessions at a version, saying what a proposal has to
contain and the date it closes. Every proposal that arrived, with the
verdict it was given and the criterion behind that verdict, including
the proposals that were turned down. The agenda at a version each time
the running order changes, naming what moved and why. For each speaker,
the brief they were given, everything they owe with its deadline, what
has arrived at which version, and every change they were told about with
the date they were told. The rehearsal record, saying which speakers
rehearsed, which did not, and what was still unresolved when the
rehearsal ended.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
