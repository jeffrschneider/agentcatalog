---
name: set-out-the-options
description: Sets out each way to meet a staffing gap or a queue about to miss, with what each gives the service levels, what it does to the other queues and what it costs, for the named person who decides. Use it when running `ref/sup/forecast-support-volume` and `ref/sup/run-the-days-queue`.
license: CC-BY-4.0
metadata:
  agent: staffing-planner
  agent-version: "1"
---

# Set out the options

## What it does

Sets out each way to meet a staffing gap or a queue about to miss, with
what each gives the service levels, what it does to the other queues and
what it costs, for the named person who decides.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Set Out What Can Be Done**
  - `ref/sup/run-the-days-queue`, activity 8 -
    [Run the Day's Queue](../../../../processes/customer-support/run-the-days-queue.md)
- **Set Out the Options for a Gap**
  - `ref/sup/forecast-support-volume`, activity 12 -
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
