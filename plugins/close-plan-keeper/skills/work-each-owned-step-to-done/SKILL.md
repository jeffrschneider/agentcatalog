---
name: work-each-owned-step-to-done
description: Holds each step that somebody else owns as a dated step inside the checklist, and works it with its owner until it is done with its evidence. Use it when running `ref/pc/form-the-fund` and `ref/pc/run-the-closing`.
license: CC-BY-4.0
metadata:
  agent: close-plan-keeper
  agent-version: "1"
---

# Work each owned step to done

## What it does

Holds each step that somebody else owns as a dated step inside the
checklist, and works it with its owner until it is done with its
evidence. In forming a fund these are the entities counsel forms, the
partnership agreement and subscription documents counsel drafts, the
filings the compliance officer makes, and the books and portals the fund
opens. In a closing they are the capital call the fund needs, the
consents, filings and approvals the closing waits on, and what the
agreements still owe once the deal has closed.

## Where it happens

The agent does this in eight activities across two reference processes.
Each one names the activity as that process words it.

- **Draft the Partnership Agreement**
  - `ref/pc/form-the-fund`, activity 9 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Draft the Subscription Documents**
  - `ref/pc/form-the-fund`, activity 11 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Form the Entities**
  - `ref/pc/form-the-fund`, activity 7 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Make the Regulatory Filings**
  - `ref/pc/form-the-fund`, activity 13 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Open the Fund's Records**
  - `ref/pc/form-the-fund`, activity 16 -
    [Form the Fund](../../../../processes/private-capital/form-the-fund.md)
- **Request the Capital Call**
  - `ref/pc/run-the-closing`, activity 3 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **Track the Post-Closing Items**
  - `ref/pc/run-the-closing`, activity 16 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)
- **Work the Closing Conditions**
  - `ref/pc/run-the-closing`, activity 4 -
    [Run the Closing](../../../../processes/private-capital/run-the-closing.md)

## What to record

The plan opened from the agreed position, with the signature date. Every
step, on either side, with one named owner and one date, and the steps
that block others marked. The buyer's approval path with the committee
dates and the person who takes it to each one. The buyer's confirmation
of the plan, kept and dated. Every chase, with the reason the owner gave
and the new date it produced. Every re-plan, showing which steps moved
and whether the signature date moved or the slack was named. The
pre-signature conditions marked done with their evidence. At close, the
plan with what slipped, why, and what to plan differently.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
