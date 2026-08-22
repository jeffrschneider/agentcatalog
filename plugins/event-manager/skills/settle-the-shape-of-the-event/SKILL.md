---
name: settle-the-shape-of-the-event
description: The agent settles what kind of event it is, how long it runs, what the budget and the target are, and what actually happens in it, down to the sessions and the order they come in. Use it when running `ref/mkt/advisory-board` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: event-manager
  agent-version: "1"
---

# Settle the shape of the event

## What it does

The agent settles what kind of event it is, how long it runs, what the
budget and the target are, and what actually happens in it, down to the
sessions and the order they come in.

## Where it happens

The agent does this in five activities across four reference processes.
Each one names the activity as that process words it.

- **Choose the Program**
  - `ref/mkt/user-conference`, activity 5 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Set the Agenda**
  - `ref/mkt/advisory-board`, activity 2 -
    [Convene Customer Advisory Board](../../../../processes/marketing/advisory-board.md)
- **Set the Conference Plan**
  - `ref/mkt/user-conference`, activity 2 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Settle the Format and Program**
  - `ref/mkt/field-event`, activity 2 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Settle the Format and the Presenters**
  - `ref/mkt/webinar`, activity 2 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)

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
