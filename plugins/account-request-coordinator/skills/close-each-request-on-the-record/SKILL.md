---
name: close-each-request-on-the-record
description: Confirms the holder is back in after a handover, records who asked, each check and how it was made, who decided and what changed, and records what each recovery and each closure taught. Use it when running `ref/sup/answer-a-data-request`, `ref/sup/close-a-customer-account` and `ref/sup/recover-access-to-an-account`.
license: CC-BY-4.0
metadata:
  agent: account-request-coordinator
  agent-version: "1"
---

# Close each request on the record

## What it does

Confirms the holder is back in after a handover, records who asked, each
check and how it was made, who decided and what changed, and records
what each recovery and each closure taught.

## Where it happens

The agent does this in six activities across three reference processes.
Each one names the activity as that process words it.

- **Close the Request on the Record**
  - `ref/sup/recover-access-to-an-account`, activity 15 -
    [Recover Access to an Account](../../../../processes/customer-support/recover-access-to-an-account.md)
- **Confirm the Holder Is Back In**
  - `ref/sup/recover-access-to-an-account`, activity 14 -
    [Recover Access to an Account](../../../../processes/customer-support/recover-access-to-an-account.md)
- **Record What the Closure Taught**
  - `ref/sup/close-a-customer-account`, activity 15 -
    [Close a Customer Account](../../../../processes/customer-support/close-a-customer-account.md)
- **Record What the Request Taught**
  - `ref/sup/recover-access-to-an-account`, activity 16 -
    [Recover Access to an Account](../../../../processes/customer-support/recover-access-to-an-account.md)
- **Record the Closure**
  - `ref/sup/close-a-customer-account`, activity 14 -
    [Close a Customer Account](../../../../processes/customer-support/close-a-customer-account.md)
- **Record the Request**
  - `ref/sup/answer-a-data-request`, activity 17 -
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
