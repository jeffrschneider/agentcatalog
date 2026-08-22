---
name: show-the-working-and-have-it-read
description: Builds each statement so that every line names its booking, its rate, its plan sentence and its date, puts it in front of the manager who has to stand behind it, and records what they accepted and what they said was wrong. Use it when running `ref/rev/calculate-commission`.
license: CC-BY-4.0
metadata:
  agent: commission-calculator
  agent-version: "1"
---

# Show the working and have it read

## What it does

Builds each statement so that every line names its booking, its rate,
its plan sentence and its date, puts it in front of the manager who has
to stand behind it, and records what they accepted and what they said
was wrong.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Have the Manager Read the Statements**
  - `ref/rev/calculate-commission`, activity 13 -
    [Calculate Commission](../../../../processes/revenue-operations/calculate-commission.md)
- **Record the Corrections**
  - `ref/rev/calculate-commission`, activity 16 -
    [Calculate Commission](../../../../processes/revenue-operations/calculate-commission.md)
- **Show the Working, Line by Line**
  - `ref/rev/calculate-commission`, activity 12 -
    [Calculate Commission](../../../../processes/revenue-operations/calculate-commission.md)

## What to record

Per run: the period boundaries, the sellers in scope, the plan version
each seller sits on, and the booking snapshot with the system, the query
and the timestamp it was taken at. Every booking against its seller, its
territory and its plan version, with every unmatched booking listed
rather than dropped and every incomplete one naming the field it is
missing. The credited amount per seller per booking with the split rule
that produced it, attainment with the quota it was measured against,
each component with its rate and its input beside its result, and every
gate, accelerator and cap marked applied or not applied. Every draw,
recoverable and clawback with the period it came from, and every held
amount with the condition it waits on and the period it is expected in.
Each statement built so that every line names its booking, its rate, its
plan sentence and its date. Then what each manager accepted and what
they said was wrong, the run at a version with its total and its
signatures, what payroll received and when, and every correction with
the plan sentence or the record that caused it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
