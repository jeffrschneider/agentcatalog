---
name: prove-the-measure-still-measures
description: Puts runs whose answer is already known through the detection, checks every signal raised in the first weeks by hand against the run it fired on, and tests the measure for outages, renamed fields and dead signals before any number is read out, so a hole is never read as compliance. Use it when running `ref/rev/instrument-a-process` and `ref/rev/review-adoption`.
license: CC-BY-4.0
metadata:
  agent: adoption-monitor
  agent-version: "1"
---

# Prove the measure still measures

## What it does

Puts runs whose answer is already known through the detection, checks
every signal raised in the first weeks by hand against the run it fired
on, and tests the measure for outages, renamed fields and dead signals
before any number is read out, so a hole is never read as compliance.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Check the Measure Still Measures**
  - `ref/rev/review-adoption`, activity 2 -
    [Review Adoption](../../../../processes/revenue-operations/review-adoption.md)
- **Test the Detection on Known Runs**
  - `ref/rev/instrument-a-process`, activity 11 -
    [Instrument a Process](../../../../processes/revenue-operations/instrument-a-process.md)
- **Watch the First Weeks**
  - `ref/rev/instrument-a-process`, activity 15 -
    [Instrument a Process](../../../../processes/revenue-operations/instrument-a-process.md)

## What to record

Per process: the watched steps, and the unwatched ones with the reason
each was left out. For each watched step, the observable difference
between a followed run and a departed one. The change request field by
field, saying what each new field records about a person, and the policy
check with the line behind every refusal and the fields the privacy
reviewer struck out. The baseline, and the detection's score against the
known runs with every miss and every false alarm listed. Every signal
raised in the first weeks, checked by hand against the run it fired on.
The steps it still cannot see. Per period: the measure's gaps and
outages marked before a number is read, the ranked departures with the
count behind each rate, and what people said, attributed to a role, with
the refusals counted as refusals.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
