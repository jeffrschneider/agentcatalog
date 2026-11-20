---
name: keep-the-traveler-reachable
description: Keeps where the traveler is each day of the trip, open only to the named people who respond to an emergency, and gives the travel and expense lead who is where when an event hits a place on the itinerary. Use it when running `ref/fin/book-business-travel`.
license: CC-BY-4.0
metadata:
  agent: travel-coordinator
  agent-version: "1"
---

# Keep the traveler reachable

## What it does

Keeps where the traveler is each day of the trip, open only to the named
people who respond to an emergency, and gives the travel and expense
lead who is where when an event hits a place on the itinerary.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Keep the Traveler's Whereabouts**
  - `ref/fin/book-business-travel`, activity 10 -
    [Book Business Travel](../../../../processes/finance/book-business-travel.md)
- **Reach the Traveler in an Emergency**
  - `ref/fin/book-business-travel`, activity 12 -
    [Book Business Travel](../../../../processes/finance/book-business-travel.md)

## What to record

Each trip leaves the request with its business reason and its cost
center, the reading against the policy at its version, the manager's
approval where the policy asks for it, the options offered with the
lowest that fit first and their cancellation terms, the traveler's
choice, and any exception with the traveler's reason and the approver's
written decision dated before the booking. Beside them sit each booking
with its reference, its fare and its terms, the itinerary as sent, each
change or cancellation with the approval behind it, and each cost passed
to the expense record. The trip closes with each unused ticket and
credit recorded for later use and the date the whereabouts were deleted.
Nothing in the record shows this agent booking outside the policy
without a written approval, booking a different fare or a higher price
than the one chosen or approved, or using the whereabouts for anything
other than reaching and helping the traveler.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
