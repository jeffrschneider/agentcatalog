---
name: build-the-invoice
description: Opens the invoice on its billing date, reads the booking at its version, checks that the usage reading is complete for a customer billed on use, builds each line from the booking and the usage, and applies the indirect tax each line carries. Use it when running `ref/fin/issue-a-customer-invoice`.
license: CC-BY-4.0
metadata:
  agent: billing-administrator
  agent-version: "1"
---

# Build the invoice

## What it does

Opens the invoice on its billing date, reads the booking at its version,
checks that the usage reading is complete for a customer billed on use,
builds each line from the booking and the usage, and applies the
indirect tax each line carries.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Apply the Indirect Tax**
  - `ref/fin/issue-a-customer-invoice`, activity 6 -
    [Issue a Customer Invoice](../../../../processes/finance/issue-a-customer-invoice.md)
- **Build the Invoice Lines**
  - `ref/fin/issue-a-customer-invoice`, activity 5 -
    [Issue a Customer Invoice](../../../../processes/finance/issue-a-customer-invoice.md)
- **Check the Usage Reading Is Complete**
  - `ref/fin/issue-a-customer-invoice`, activity 4 -
    [Issue a Customer Invoice](../../../../processes/finance/issue-a-customer-invoice.md)
- **Open the Invoice**
  - `ref/fin/issue-a-customer-invoice`, activity 1 -
    [Issue a Customer Invoice](../../../../processes/finance/issue-a-customer-invoice.md)
- **Supply the Booking at Its Version**
  - `ref/fin/issue-a-customer-invoice`, activity 2 -
    [Issue a Customer Invoice](../../../../processes/finance/issue-a-customer-invoice.md)

## What to record

Each invoice leaves its billing date, the booking at its version with
each field naming its clause, the usage reading with its date or the
reason it was held, each line with its price, its tax and the place it
was supplied, the check against the local rules and against the booking
with the total beside the last invoice, and the billing lead's approval
where the policy asks for it. Beside them sit the number in its series,
the dates it was issued and sent, the channel it went by, the customer's
receipt or the portal's rejection with its reason, and how a rejected
invoice was put right. Each disputed invoice leaves the recompute beside
the original with every input where they differ, the credit note or
replacement at its version for exactly what was decided with its
approval, and the cause sent to its owner. Nothing in the record shows
this agent editing an issued invoice, approving an invoice or a credit
note, or billing on an estimate nobody approved.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
