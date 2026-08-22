---
name: report-how-the-event-did
description: "The agent writes the account of the event: who came, what it cost, what it produced, and how that compares with what the event was asked to do. Use it when running `ref/mkt/field-event` and 3 other reference processes."
license: CC-BY-4.0
metadata:
  agent: event-manager
  agent-version: "1"
---

# Report how the event did

## What it does

The agent writes the account of the event: who came, what it cost, what
it produced, and how that compares with what the event was asked to do.

## Where it happens

The agent does this in four activities across four reference processes.
Each one names the activity as that process words it.

- **Report How the Event Did**
  - `ref/mkt/field-event`, activity 15 -
    [Host Field Event](../../../../processes/marketing/field-event.md)
- **Report How the Session Did**
  - `ref/mkt/webinar`, activity 17 -
    [Produce Webinar](../../../../processes/marketing/webinar.md)
- **Report the Conference**
  - `ref/mkt/user-conference`, activity 16 -
    [Host User Conference](../../../../processes/marketing/user-conference.md)
- **Report the Show**
  - `ref/mkt/trade-show`, activity 15 -
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
