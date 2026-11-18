---
name: turn-each-letter-into-obligations
description: Helps counsel draft the side letter with every clause tied to its closed ask, records each promise as an obligation with its owner, what sets it off and its due date, and loads each agreed letter at the close so its obligations are in force from the signing. Use it when running `ref/pc/hold-a-fund-close` and `ref/pc/negotiate-the-fund-terms-and-side-letters`.
license: CC-BY-4.0
metadata:
  agent: side-letter-keeper
  agent-version: "1"
---

# Turn each letter into obligations

## What it does

Helps counsel draft the side letter with every clause tied to its closed
ask, records each promise as an obligation with its owner, what sets it
off and its due date, and loads each agreed letter at the close so its
obligations are in force from the signing.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Draft the Side Letter**
  - `ref/pc/negotiate-the-fund-terms-and-side-letters`, activity 14 -
    [Negotiate the Fund Terms and Side Letters](../../../../processes/private-capital/negotiate-the-fund-terms-and-side-letters.md)
- **Load the Side Letters to Be Signed**
  - `ref/pc/hold-a-fund-close`, activity 7 -
    [Hold a Fund Close](../../../../processes/private-capital/hold-a-fund-close.md)
- **Record Each Promise as an Obligation**
  - `ref/pc/negotiate-the-fund-terms-and-side-letters`, activity 16 -
    [Negotiate the Fund Terms and Side Letters](../../../../processes/private-capital/negotiate-the-fund-terms-and-side-letters.md)

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
