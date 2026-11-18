---
name: screen-against-the-lists
description: The agent screens investors and their owners, target companies and their leaders, and the firm's own people and providers against sanctions lists, the anti-money laundering rules, adverse records and the events that would disqualify an offering. Use it when running `ref/pc/form-the-fund`, `ref/pc/hold-a-fund-close` and `ref/pc/run-legal-and-compliance-diligence`.
license: CC-BY-4.0
metadata:
  agent: supplier-check
  agent-version: "1"
---

# Screen against the lists

## What it does

The agent screens investors and their owners, target companies and their
leaders, and the firm's own people and providers against sanctions
lists, the anti-money laundering rules, adverse records and the events
that would disqualify an offering. Every hit goes to the chief
compliance officer with what was found and where, and the agent records
the decision it is given without clearing any hit itself.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Check No One Disqualifies the Offering**
  - `ref/pc/form-the-fund`, activity 8 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Clear the Screening Hits**
  - `ref/pc/hold-a-fund-close`, activity 6 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
  - `ref/pc/run-legal-and-compliance-diligence`, activity 15 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)
- **Screen Each Investor and Its Owners**
  - `ref/pc/hold-a-fund-close`, activity 5 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
- **Screen the Company and Its Leaders**
  - `ref/pc/run-legal-and-compliance-diligence`, activity 14 -
    [Run Legal and Compliance Diligence](../../../../processes/private-capital/run-legal-and-compliance-diligence.md)

## What to record

It leaves a scoring sheet for each candidate at a version, naming the
requirements list and the version it scored against, with one row per
requirement carrying the verdict and the evidence behind it. The
evidence names the demonstration step, the document, or the reference
call it came from, so a person can check a verdict without asking the
agent what it meant. A requirement it could not test is recorded as not
tested, with the reason it could not be tested. When a candidate revises
its material, the rescore says what changed, what was run again, and
what was carried over from the earlier score. It records the date each
candidate's material arrived and the date it was scored.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
