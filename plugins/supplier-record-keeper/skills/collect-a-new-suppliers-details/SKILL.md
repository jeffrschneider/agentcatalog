---
name: collect-a-new-suppliers-details
description: Takes in the request for a supplier with no record, and collects its legal name, address, contacts, payment terms and bank details in one request, with the tax forms and numbers the local rules require for each place the company buys from it. Use it when running `ref/fin/set-up-a-supplier`.
license: CC-BY-4.0
metadata:
  agent: supplier-record-keeper
  agent-version: "1"
---

# Collect a new suppliers details

## What it does

Takes in the request for a supplier with no record, and collects its
legal name, address, contacts, payment terms and bank details in one
request, with the tax forms and numbers the local rules require for each
place the company buys from it.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Collect What Tax Rules Require**
  - `ref/fin/set-up-a-supplier`, activity 4 -
    [Set Up a Supplier](../../../../processes/finance/set-up-a-supplier.md)
- **Collect the Supplier's Details**
  - `ref/fin/set-up-a-supplier`, activity 3 -
    [Set Up a Supplier](../../../../processes/finance/set-up-a-supplier.md)
- **Take in the Request for a Supplier**
  - `ref/fin/set-up-a-supplier`, activity 1 -
    [Set Up a Supplier](../../../../processes/finance/set-up-a-supplier.md)

## What to record

Each setup leaves the request with who asked and the order or the choice
behind it, the duplicate check, each detail and tax document with its
source and the date it came, the public record and screening results
with any hit decided in writing, the bank details with who confirmed
them by a call to a contact found apart from the request, and the record
at its version with the approver named and the date it opened. Each
change leaves the request exactly as it arrived with its channel, its
sender and its date, the hold with every payment that kept going to the
account on the record, the checks the wire-check agent made, the call
with the person who made it, the approval, the new details with their
effective date beside the old ones with theirs, the notice to the
supplier, and the first payment confirmed or the report of a suspected
fraud. Each record closed for disuse leaves the date it was last used
and the date it closed. Nothing in the record shows this agent approving
a record, confirming bank details or applying a change before its
approval.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
