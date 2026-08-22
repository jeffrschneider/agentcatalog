---
name: report-the-departures
description: Ranks the steps that are departed from most, asks the people who departed why in their own words, and hands the numbers, the baseline and the blind spots to the review without blaming anybody for them. Use it when running `ref/rev/instrument-a-process` and `ref/rev/review-adoption`.
license: CC-BY-4.0
metadata:
  agent: adoption-monitor
  agent-version: "1"
---

# Report the departures

## What it does

Ranks the steps that are departed from most, asks the people who
departed why in their own words, and hands the numbers, the baseline and
the blind spots to the review without blaming anybody for them.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Ask the People Who Departed Why**
  - `ref/rev/review-adoption`, activity 5 -
    [Review Adoption](../../../../processes/revenue-operations/review-adoption.md)
- **Hand the Measure to the Review**
  - `ref/rev/instrument-a-process`, activity 16 -
    [Instrument a Process](../../../../processes/revenue-operations/instrument-a-process.md)
- **Rank the Departures**
  - `ref/rev/review-adoption`, activity 3 -
    [Review Adoption](../../../../processes/revenue-operations/review-adoption.md)

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
