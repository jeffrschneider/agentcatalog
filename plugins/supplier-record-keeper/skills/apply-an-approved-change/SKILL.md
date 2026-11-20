---
name: apply-an-approved-change
description: Applies an approved change on its date with the old details kept with their dates, tells the supplier through the contact on file, and closes the change with who asked, who confirmed and who approved. Use it when running `ref/fin/change-a-suppliers-bank-details`.
license: CC-BY-4.0
metadata:
  agent: supplier-record-keeper
  agent-version: "1"
---

# Apply an approved change

## What it does

Applies an approved change on its date with the old details kept with
their dates, tells the supplier through the contact on file, and closes
the change with who asked, who confirmed and who approved.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Apply the Change on Its Date**
  - `ref/fin/change-a-suppliers-bank-details`, activity 10 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Close the Change on the Record**
  - `ref/fin/change-a-suppliers-bank-details`, activity 14 -
    [Change a Supplier's Bank Details](../../../../processes/finance/change-a-suppliers-bank-details.md)
- **Tell the Supplier**
  - `ref/fin/change-a-suppliers-bank-details`, activity 11 -
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
