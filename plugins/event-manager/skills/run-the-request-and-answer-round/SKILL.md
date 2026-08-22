---
name: run-the-request-and-answer-round
description: The agent runs a round where every function submits what it is asking for in one format by one date, and then tells each function what it was given and the rules that come with it. Use it when running `ref/mkt/set-marketing-budget`.
license: CC-BY-4.0
metadata:
  agent: event-manager
  agent-version: "1"
---

# Run the request and answer round

## What it does

The agent runs a round where every function submits what it is asking
for in one format by one date, and then tells each function what it was
given and the rules that come with it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Collect What Each Function Asks For**
  - `ref/mkt/set-marketing-budget`, activity 4 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)
- **Tell Every Function What It Has**
  - `ref/mkt/set-marketing-budget`, activity 14 -
    [Set Marketing Budget](../../../../processes/marketing/set-marketing-budget.md)

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
