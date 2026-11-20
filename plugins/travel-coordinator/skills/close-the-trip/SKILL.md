---
name: close-the-trip
description: Passes each booking's cost to the expense record, records each unused ticket and credit once the traveler is home, deletes the whereabouts under the retention rule, and records what the trip taught. Use it when running `ref/fin/book-business-travel`.
license: CC-BY-4.0
metadata:
  agent: travel-coordinator
  agent-version: "1"
---

# Close the trip

## What it does

Passes each booking's cost to the expense record, records each unused
ticket and credit once the traveler is home, deletes the whereabouts
under the retention rule, and records what the trip taught.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Close the Trip**
  - `ref/fin/book-business-travel`, activity 14 -
    [Book Business Travel](../../../../processes/finance/book-business-travel.md)
- **Pass the Costs to the Expense Record**
  - `ref/fin/book-business-travel`, activity 13 -
    [Book Business Travel](../../../../processes/finance/book-business-travel.md)
- **Record What the Trip Taught**
  - `ref/fin/book-business-travel`, activity 15 -
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
