---
name: apply-the-letters-to-a-call
description: Takes out every investor the agreement or its side letter excuses from the investment, with the clause that excuses it, and applies the notice period, caps, currency and delivery each investor was promised. Use it when running `ref/pc/issue-a-capital-call`.
license: CC-BY-4.0
metadata:
  agent: side-letter-keeper
  agent-version: "1"
---

# Apply the letters to a call

## What it does

Takes out every investor the agreement or its side letter excuses from
the investment, with the clause that excuses it, and applies the notice
period, caps, currency and delivery each investor was promised.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Apply the Side Letter Terms**
  - `ref/pc/issue-a-capital-call`, activity 5 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)
- **Take Out the Excused Investors**
  - `ref/pc/issue-a-capital-call`, activity 4 -
    [Issue a Capital Call](../../../../processes/private-capital/issue-a-capital-call.md)

## What to record

Per letter: the letter at its signed version, and each clause held as an
obligation naming its owner, what sets it off, its due date and the
closed ask it came from. Per negotiation: the letters already signed for
the fund, which investors hold an MFN right that would reach each ask,
and each term of the new letter marked electable or excluded, naming the
MFN exclusion that excludes it. Per final close: the terms sent to each
MFN holder with the date its elections were due, each election received,
and each elected term added as an obligation with the date it takes
effect. Per capital call: the excused investors with the clause that
excuses each and how their share is carried by the others, and per
investor the notice period, caps, currency and delivery applied. Per fee
period: each discount, early-closer rate and waiver applied with its
clause, the offsets worked out at the share the agreement sets, and each
charge against every cap in the agreement and each letter with the
running total for the year and any excess named as the firm's. Per
quarter: each investor's reporting promises on content, template,
currency, timing and extra reports, each statement checked with any
missing item named against its clause, and any missed date recorded
against the letter it breaks. An auditor can take any clause of any side
letter and find every call, fee period and report it was checked
against.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
