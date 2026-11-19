---
name: send-and-revise-the-offer
description: Sends the approved letter the same day the recruiter makes the offer, checks each ask the candidate makes against the approved limits, and writes each new version of the letter with every change marked. Use it when running `ref/hr/make-an-offer`.
license: CC-BY-4.0
metadata:
  agent: offer-builder
  agent-version: "1"
---

# Send and revise the offer

## What it does

Sends the approved letter the same day the recruiter makes the offer,
checks each ask the candidate makes against the approved limits, and
writes each new version of the letter with every change marked.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Check Each Ask Against the Limits**
  - `ref/hr/make-an-offer`, activity 11 -
    [Make an Offer](../../../../processes/human-resources/make-an-offer.md)
- **Make the Offer**
  - `ref/hr/make-an-offer`, activity 9 -
    [Make an Offer](../../../../processes/human-resources/make-an-offer.md)
- **Revise the Offer**
  - `ref/hr/make-an-offer`, activity 13 -
    [Make an Offer](../../../../processes/human-resources/make-an-offer.md)

## What to record

Each offer leaves the decision with the reserves in order, the outcome
of the checks read as clear, decided or conditional with nothing about
what a check found, the agreed terms with the compensation-analyst
agent's check beside them, and each version of the letter with its
expiry date, any condition it carries and every change from the last
version marked. Beside each version sit the approvers' signatures in the
set order and their dates, and the date the recruiter made the offer and
the letter went out. Each ask is read against the limits and marked
inside or past them, with the approvers' written answer to any ask past
them. The run closes with the signed acceptance, the agreed start date
and the final terms, a conditional offer confirmed once the checks
cleared, and the hire handed to onboarding. Nothing in the record shows
this agent approving, changing or withdrawing an offer on its own.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
