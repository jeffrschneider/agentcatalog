---
name: supply-what-is-earned-and-not-yet-paid
description: Gives the accountants the commission earned in a period and not yet paid, line by line from the run at its version, each line naming the deal and the plan behind it, and marks the figures incomplete when the run has not computed the whole period by the cutoff. Use it when running `ref/fin/book-the-period-end-accruals`.
license: CC-BY-4.0
metadata:
  agent: commission-calculator
  agent-version: "1"
---

# Supply what is earned and not yet paid

## What it does

Gives the accountants the commission earned in a period and not yet
paid, line by line from the run at its version, each line naming the
deal and the plan behind it, and marks the figures incomplete when the
run has not computed the whole period by the cutoff.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Take In the Commission Earned**
  - `ref/fin/book-the-period-end-accruals`, activity 5 -
    [Book the Period-End Accruals](../../../../processes/finance/book-the-period-end-accruals.md)

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
