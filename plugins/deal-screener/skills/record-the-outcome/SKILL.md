---
name: record-the-outcome
description: Opens the opportunity with its named owner when a partner decides to meet, and records the decision, its reason, the time the answer took, and for a sale the bank's reply and the price the company sold for. Use it when running `ref/pc/respond-to-a-sale-process` and `ref/pc/screen-an-inbound-pitch`.
license: CC-BY-4.0
metadata:
  agent: deal-screener
  agent-version: "1"
---

# Record the outcome

## What it does

Opens the opportunity with its named owner when a partner decides to
meet, and records the decision, its reason, the time the answer took,
and for a sale the bank's reply and the price the company sold for.

## Where it happens

The agent does this in three activities across two reference processes.
Each one names the activity as that process words it.

- **Open the Opportunity**
  - `ref/pc/screen-an-inbound-pitch`, activity 17 -
    [Screen an Inbound Pitch](../../../../processes/private-capital/screen-an-inbound-pitch.md)
- **Record the Decision and the Time**
  - `ref/pc/screen-an-inbound-pitch`, activity 18 -
    [Screen an Inbound Pitch](../../../../processes/private-capital/screen-an-inbound-pitch.md)
- **Record the Outcome**
  - `ref/pc/respond-to-a-sale-process`, activity 18 -
    [Respond to a Sale Process](../../../../processes/private-capital/respond-to-a-sale-process.md)

## What to record

Per teaser or pitch: its arrival with the sender, the channel, the
referrer, and for a sale the bank, the seller and every date in the
process letter; the check that it may be read, with any terms attached
and the people who read it; the match against the CRM, the pipeline and
every sector map, naming any past meeting, bid, pass or owner; the
reading with each claim of the deck or the seller marked as a claim; the
mandate test with the clause behind each result at the version read; the
thesis it fits and what would have to be true; the referral with any tie
to the company written in; the screen note at its version with its
proposed answer and reason; and the partner's decision with its reason
and who made it. For a pitch: the one list of missing questions with its
date, the opportunity opened with its owner, and how long the answer
took against the promise. For a sale: the memorandum logged with the
people allowed to read it; the indication as sent, with the range, the
basis, the financing, the conditions, the diligence still needed and the
approvals, matching the range the partners decided; or the withdrawal
sent before the deadline, with the return or destruction of the material
recorded; and the bank's reply, the firm's place, and the price the
company sold for once it is known. An auditor can check that every pitch
got an answer, that every pass gives its reason in the terms of the
mandate or a thesis, and that no figure outside the decided range went
to a bank.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
