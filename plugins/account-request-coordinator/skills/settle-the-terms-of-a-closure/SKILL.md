---
name: settle-the-terms-of-a-closure
description: Sets each request to close against the agreement and the local rules, lists the invoices still open, offers the customer a copy of its data, sets out what each system keeps and until when, and confirms the closing date with the customer. Use it when running `ref/sup/close-a-customer-account`.
license: CC-BY-4.0
metadata:
  agent: account-request-coordinator
  agent-version: "1"
---

# Settle the terms of a closure

## What it does

Sets each request to close against the agreement and the local rules,
lists the invoices still open, offers the customer a copy of its data,
sets out what each system keeps and until when, and confirms the closing
date with the customer.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Confirm the Closing Date with the Customer**
  - `ref/sup/close-a-customer-account`, activity 9 -
    [Close a Customer Account](../../../../processes/customer-support/close-a-customer-account.md)
- **List the Invoices Still Open**
  - `ref/sup/close-a-customer-account`, activity 6 -
    [Close a Customer Account](../../../../processes/customer-support/close-a-customer-account.md)
- **Offer the Customer Its Data**
  - `ref/sup/close-a-customer-account`, activity 7 -
    [Close a Customer Account](../../../../processes/customer-support/close-a-customer-account.md)
- **Set What Each System Keeps**
  - `ref/sup/close-a-customer-account`, activity 8 -
    [Close a Customer Account](../../../../processes/customer-support/close-a-customer-account.md)
- **Set the Request Against the Agreement**
  - `ref/sup/close-a-customer-account`, activity 5 -
    [Close a Customer Account](../../../../processes/customer-support/close-a-customer-account.md)

## What to record

Each recovery leaves the request exactly as it arrived with its headers
and attachments, the hold on the account with every change it stopped,
the contacts on file with the date each was put there, each check the
identity-check agent made and how, who confirmed through which details
on file and when, the notice to the existing contacts and any objection,
the handover as prepared and who decided it, the notice that access was
restored or control moved, and the first sign-in, or the refusal and the
report to `<your security team>`. Each closure leaves the request in the
customer's own words, the authority check, when the account owner was
told, the agreement's position and the earliest closing date, the
invoices still open, the customer's choice about its data, what each
system keeps and until when, the date confirmed with the customer, who
closed the account and when, and what the customer, Finance and the
account owner were told. Each data request leaves its log entry with its
deadline, the acknowledgment, the identity and authority checks, every
system searched with what was found there, the other people's details
set aside, the privacy lead's decision with its reasons, each correction
and deletion with the owner who made it and the search that confirmed
it, and the answer as prepared and as sent. Nothing in the record shows
this agent handing over access, closing an account, releasing,
correcting or deleting data, or using a contact detail that only the
request supplied.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
