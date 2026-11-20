---
name: run-a-data-request
description: Logs each data request with its deadline, acknowledges it in the approved words, finds the data in every system on the data map, sets aside other people's details, and searches every system again to confirm that what was deleted is gone. Use it when running `ref/sup/answer-a-data-request`.
license: CC-BY-4.0
metadata:
  agent: account-request-coordinator
  agent-version: "1"
---

# Run a data request

## What it does

Logs each data request with its deadline, acknowledges it in the
approved words, finds the data in every system on the data map, sets
aside other people's details, and searches every system again to confirm
that what was deleted is gone.

## Where it happens

The agent does this in five activities across one reference process.
Each one names the activity as that process words it.

- **Acknowledge the Request**
  - `ref/sup/answer-a-data-request`, activity 3 -
    [Answer a Data Request](../../../../processes/customer-support/answer-a-data-request.md)
- **Confirm What Is Gone**
  - `ref/sup/answer-a-data-request`, activity 13 -
    [Answer a Data Request](../../../../processes/customer-support/answer-a-data-request.md)
- **Find the Data in Every System**
  - `ref/sup/answer-a-data-request`, activity 6 -
    [Answer a Data Request](../../../../processes/customer-support/answer-a-data-request.md)
- **Log the Request with Its Deadline**
  - `ref/sup/answer-a-data-request`, activity 2 -
    [Answer a Data Request](../../../../processes/customer-support/answer-a-data-request.md)
- **Set Aside Other People's Details**
  - `ref/sup/answer-a-data-request`, activity 8 -
    [Answer a Data Request](../../../../processes/customer-support/answer-a-data-request.md)

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
