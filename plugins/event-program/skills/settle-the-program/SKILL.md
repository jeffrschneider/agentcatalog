---
name: settle-the-program
description: Decides what the event carries and in what order. Use it when running `ref/mkt/advisory-board` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: event-program
  agent-version: "1"
---

# Settle the program

## What it does

Decides what the event carries and in what order. It settles the kind of
session and how long it runs, picks the talks and the keynotes, puts the
questions or the sessions into an order, and says who presents each one.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Choose the Program**
  - `ref/mkt/user-conference`, activity 5 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Set the Agenda**
  - `ref/mkt/advisory-board`, activity 2 -
    [Convene Customer Advisory Board](../../../../processes/marketing/advisory-board.md)
- **Settle the Format and Program**
  - `ref/mkt/field-event`, activity 2 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Settle the Format and the Presenters**
  - `ref/mkt/webinar`, activity 2 -
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
