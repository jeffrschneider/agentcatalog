---
name: price-a-draft-plan-on-paper
description: Runs a draft plan over the awkward deals the business really sells and says what it would pay for each one. Use it when running `ref/rev/design-a-comp-plan`.
license: CC-BY-4.0
metadata:
  agent: commission-calculator
  agent-version: "1"
---

# Price a draft plan on paper

## What it does

Runs a draft plan over the awkward deals the business really sells and
says what it would pay for each one. Builds the worked examples the way
the real run will compute them, and hears the published wording at the
same time as the managers who have to explain it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Brief the Managers and the Calculator**
  - `ref/rev/design-a-comp-plan`, activity 15 -
    [Design a Compensation Plan](../../../../processes/revenue-operations/design-a-comp-plan.md)
- **Build the Worked Examples**
  - `ref/rev/design-a-comp-plan`, activity 12 -
    [Design a Compensation Plan](../../../../processes/revenue-operations/design-a-comp-plan.md)
- **Test the Plan Against Awkward Cases**
  - `ref/rev/design-a-comp-plan`, activity 7 -
    [Design a Compensation Plan](../../../../processes/revenue-operations/design-a-comp-plan.md)

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
