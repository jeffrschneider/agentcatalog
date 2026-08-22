---
name: compute-what-a-seller-earned
description: Measures attainment against that seller's own quota and computes each component with the rate and the input stored next to the result. Use it when running `ref/rev/calculate-commission`.
license: CC-BY-4.0
metadata:
  agent: commission-calculator
  agent-version: "1"
---

# Compute what a seller earned

## What it does

Measures attainment against that seller's own quota and computes each
component with the rate and the input stored next to the result. Gates,
accelerators and caps go on in the order the plan sets, each marked
applied or not applied, draws and clawbacks are netted, and anything not
yet payable is held with the condition it waits on.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Apply Gates, Accelerators and Caps**
  - `ref/rev/calculate-commission`, activity 8 -
    [Calculate Commission](../../../../processes/revenue-operations/calculate-commission.md)
- **Compute Each Component**
  - `ref/rev/calculate-commission`, activity 7 -
    [Calculate Commission](../../../../processes/revenue-operations/calculate-commission.md)
- **Hold Back What Is Not Yet Payable**
  - `ref/rev/calculate-commission`, activity 10 -
    [Calculate Commission](../../../../processes/revenue-operations/calculate-commission.md)
- **Measure Attainment**
  - `ref/rev/calculate-commission`, activity 6 -
    [Calculate Commission](../../../../processes/revenue-operations/calculate-commission.md)
- **Net Draws and Clawbacks**
  - `ref/rev/calculate-commission`, activity 9 -
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
