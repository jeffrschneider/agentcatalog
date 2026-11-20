---
name: work-out-the-people-needed
description: Opens each period's forecast from the last version, turns the requests into the people each channel and interval needs for its service level, adds the time away from cases, sets the need beside the team, says what a candidate service level would take, and publishes the forecast at a version. Use it when running `ref/sup/forecast-support-volume` and `ref/sup/set-a-service-level-policy`.
license: CC-BY-4.0
metadata:
  agent: staffing-planner
  agent-version: "1"
---

# Work out the people needed

## What it does

Opens each period's forecast from the last version, turns the requests
into the people each channel and interval needs for its service level,
adds the time away from cases, sets the need beside the team, says what
a candidate service level would take, and publishes the forecast at a
version.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Add the Time Away from Cases**
  - `ref/sup/forecast-support-volume`, activity 10 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)
- **Open the Period's Forecast**
  - `ref/sup/forecast-support-volume`, activity 1 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)
- **Publish the Forecast**
  - `ref/sup/forecast-support-volume`, activity 15 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)
- **Say What Each Would Take in People**
  - `ref/sup/set-a-service-level-policy`, activity 7 -
    [Set a Service Level Policy](../../../../processes/customer-support/set-a-service-level-policy.md)
- **Set the Need Beside the Team**
  - `ref/sup/forecast-support-volume`, activity 11 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)
- **Turn the Requests into People Needed**
  - `ref/sup/forecast-support-volume`, activity 9 -
    [Forecast Support Volume](../../../../processes/customer-support/forecast-support-volume.md)

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
