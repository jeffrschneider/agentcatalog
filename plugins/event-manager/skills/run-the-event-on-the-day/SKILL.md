---
name: run-the-event-on-the-day
description: "The agent runs the event while it is happening: people are checked in, the program keeps to time, every visitor is recorded, and the calls that have to be made on the day get made and written down. Use it when running `ref/mkt/advisory-board` and 4 other reference processes."
license: CC-BY-4.0
metadata:
  agent: event-manager
  agent-version: "1"
---

# Run the event on the day

## What it does

The agent runs the event while it is happening: people are checked in,
the program keeps to time, every visitor is recorded, and the calls that
have to be made on the day get made and written down.

## Where it happens

The agent does this in four activities across five reference processes.
Each one names the activity as that process words it.

- **Run the Event**
  - `ref/mkt/field-event`, activity 12 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Run the Session**
  - `ref/mkt/advisory-board`, activity 11 -
    [Convene Customer Advisory Board](../../../../processes/marketing/advisory-board.md)
  - `ref/mkt/webinar`, activity 12 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)
- **Run the Show**
  - `ref/mkt/user-conference`, activity 13 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Run the Show Days**
  - `ref/mkt/trade-show`, activity 12 -
    [Exhibit at Trade Show](../../../../processes/marketing/trade-show.md)

## What to record

The event plan lands at a version and says what the event has to
deliver, what each agent owes, and when each piece is due. The deadline
list lands at a version, and a dated record goes in each time a piece
lands or slips. The agent leaves the CONVENED and DONE records of the
briefing, the roll-calls, the approvals and the debrief. The invitation
and attendance record says who was invited, who registered and who came.
Every call made on the day is recorded with the time it was made and the
reason for it. The report after the event sets what happened beside what
the event was asked to do, and it goes out on its date whether or not
every source answered.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
