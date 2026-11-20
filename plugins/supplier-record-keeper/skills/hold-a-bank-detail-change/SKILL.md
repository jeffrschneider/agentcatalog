---
name: hold-a-bank-detail-change
description: Logs a request to change a supplier's bank details as it arrived, keeps the message and its attachments unchanged as evidence, and holds the change so every payment keeps going to the account on the record. Use it when running `ref/fin/change-a-suppliers-bank-details`.
license: CC-BY-4.0
metadata:
  agent: supplier-record-keeper
  agent-version: "1"
---

# Hold a bank detail change

## What it does

Logs a request to change a supplier's bank details as it arrived, keeps
the message and its attachments unchanged as evidence, and holds the
change so every payment keeps going to the account on the record.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Hold the Change**
  - `ref/fin/change-a-suppliers-bank-details`, activity 3 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Keep the Request as Evidence**
  - `ref/fin/change-a-suppliers-bank-details`, activity 2 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Take in the Request**
  - `ref/fin/change-a-suppliers-bank-details`, activity 1 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)

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
