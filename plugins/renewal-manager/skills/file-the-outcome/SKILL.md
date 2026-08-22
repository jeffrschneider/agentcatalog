---
name: file-the-outcome
description: Writes down why the term grew, held or shrank, and records a save or a departure with what was tried and what the customer said, in a form the next renewal can read. Use it when running `ref/sls/close-a-renewal` and `ref/sls/work-a-churn-risk`.
license: CC-BY-4.0
metadata:
  agent: renewal-manager
  agent-version: "1"
---

# File the outcome

## What it does

Writes down why the term grew, held or shrank, and records a save or a
departure with what was tried and what the customer said, in a form the
next renewal can read.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Record What Was Learned**
  - `ref/sls/close-a-renewal`, activity 15 -
    [Close a Renewal](../../../../processes/sales/close-a-renewal.md)
- **Record the Save or the Departure**
  - `ref/sls/work-a-churn-risk`, activity 15 -
    [Work a Churn Risk](../../../../processes/sales/work-a-churn-risk.md)

## What to record

Per renewal: the clock, opened from the agreement's own dates, with the
date the position is due. The agreement as read, with a settled reading
attached to any clause that could be read two ways. The entitlements at
their signed level with the amendments. The commitments made at
signature and still open, each with who owes it and since when. The
shape of the next term and the reason for it. The ask and the floor at
the version a person approved, with that person named. The brief at a
version, with the usage and the standing attached rather than
summarized. The customer's own words, kept rather than replaced by a
summary. What carries over, what is dropped, what is added. A smaller
term recorded beside the old price with its distance from the floor
stated. The signed agreement, and the booked term set against it line
for line. Why the term grew, held or shrank, in a form the next renewal
can read.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
