---
name: close-the-offer
description: Records the signed acceptance and the start date, confirms a conditional offer once the checks clear, hands the hire to onboarding, and records what the asks and the answers taught. Use it when running `ref/hr/make-an-offer`.
license: CC-BY-4.0
metadata:
  agent: offer-builder
  agent-version: "1"
---

# Close the offer

## What it does

Records the signed acceptance and the start date, confirms a conditional
offer once the checks clear, hands the hire to onboarding, and records
what the asks and the answers taught.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Confirm a Conditional Offer**
  - `ref/hr/make-an-offer`, activity 16 -
    [Make an Offer](../../../../processes/human-resources/make-an-offer.md)
- **Hand the Hire to Onboarding**
  - `ref/hr/make-an-offer`, activity 18 -
    [Make an Offer](../../../../processes/human-resources/make-an-offer.md)
- **Record What the Offer Taught**
  - `ref/hr/make-an-offer`, activity 19 -
    [Make an Offer](../../../../processes/human-resources/make-an-offer.md)
- **Record the Acceptance**
  - `ref/hr/make-an-offer`, activity 15 -
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
