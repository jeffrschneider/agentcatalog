---
name: handle-a-swap
description: Takes in each shift swap a support specialist asks for, checks the channel's cover and the working time rules for both people as the schedule would stand after it, and writes each approved swap into the schedule. Use it when running `ref/sup/build-the-support-schedule`.
license: CC-BY-4.0
metadata:
  agent: staffing-planner
  agent-version: "1"
---

# Handle a swap

## What it does

Takes in each shift swap a support specialist asks for, checks the
channel's cover and the working time rules for both people as the
schedule would stand after it, and writes each approved swap into the
schedule.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check the Swap for Cover**
  - `ref/sup/build-the-support-schedule`, activity 14 -
    [Build the Support Schedule](../../../../processes/customer-support/build-the-support-schedule.md)
- **Take In a Swap Request**
  - `ref/sup/build-the-support-schedule`, activity 13 -
    [Build the Support Schedule](../../../../processes/customer-support/build-the-support-schedule.md)
- **Update the Published Schedule**
  - `ref/sup/build-the-support-schedule`, activity 16 -
    [Build the Support Schedule](../../../../processes/customer-support/build-the-support-schedule.md)

## What to record

Each forecast leaves the version it started from, the people needed by
channel and interval with the method and every input, the time away from
cases, the need set beside the team with each gap by channel, interval
and date, the options for each gap with what each gives and costs, the
head of support's decision, and the version published. Each schedule
leaves the people, the leave and the rules it was built on at their
versions, each draft, each shift checked against the rules, each
interval's cover, the team leads' objections, the version approved and
who approved it, and each swap with its check, its decision and the new
version. Each day leaves the people on each channel against the plan,
each queue at risk with the options set out and the team lead's
decision, each move and each call for cover with the rules checked, and
the coverage by channel and interval. Each after-hours period leaves who
was on call and confirmed, each page passed down the rota, and the
morning team set against the held queue. Each candidate service level
leaves the people it would take by interval. Nothing in the record shows
this agent approving a schedule, a swap or leave, deciding a gap or a
move, or reporting a named person's time, breaks or adherence.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
