---
name: name-the-approvers
description: Answers each request for approval in another process with the approvers, the releasers and the stand-ins the version in force names for that kind of decision and that amount, leaving out anyone who prepared or asked for the item. Use it when running `ref/fin/approve-an-investment-case` and 9 other reference processes.
license: CC-BY-4.0
metadata:
  agent: delegation-keeper
  agent-version: "1"
---

# Name the approvers

## What it does

Answers each request for approval in another process with the approvers,
the releasers and the stand-ins the version in force names for that kind
of decision and that amount, leaving out anyone who prepared or asked
for the item.

## Where it happens

The agent does this in six activities across ten reference processes.
Each one names the activity as that process words it.

- **Find the Approvers**
  - `ref/fin/post-a-manual-journal-entry`, activity 6 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)
- **Look Up the Approver**
  - `ref/fin/book-business-travel`, activity 6 -
    [Book Business Travel](../../../../processes/finance/book-business-travel.md)
  - `ref/fin/issue-a-company-card`, activity 3 -
    [Issue a Company Card](../../../../processes/finance/issue-a-company-card.md)
- **Name the Approver**
  - `ref/fin/process-a-supplier-invoice`, activity 8 -
    [Process a Supplier Invoice](../../../../processes/finance/process-a-supplier-invoice.md)
  - `ref/fin/set-a-customers-credit-limit`, activity 8 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)
- **Name the Approver and the Releasers**
  - `ref/fin/move-cash-between-accounts`, activity 5 -
    [Move Cash Between Accounts](../../../../processes/finance/move-cash-between-accounts.md)
- **Name the Approvers**
  - `ref/fin/approve-an-investment-case`, activity 2 -
    [Approve an Investment Case](../../../../processes/finance/approve-an-investment-case.md)
  - `ref/fin/change-a-bank-account-or-signer`, activity 4 -
    [Change a Bank Account or Signer](../../../../processes/finance/change-a-bank-account-or-signer.md)
  - `ref/fin/issue-a-purchase-order`, activity 7 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Read the Approvers the Delegation Names**
  - `ref/fin/publish-a-finance-policy`, activity 5 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)

## What to record

Each change leaves the reason behind it with the decision, the role
change, the finding or the review date on the record, the version in
force as it was read, how the approvals since it ran with each one sent
above its level, given by a stand-in, matching no line or stopped, each
version of the draft with every change marked and its stand-ins named,
the check for gaps and clashes with each line drafted again, counsel's
points, the approval by the board or the people it names, the version
published with its effective date, and each change handed to the owner
of the process that carries it out. In every other process each request
leaves the approvers and stand-ins named with the version they were read
from, and each approval checked as counting or held with the reason,
such as an approver the version does not name, an amount past the
approver's limit or an approval by the person who prepared the item.
Nothing in the record shows this agent approving an item, changing a
line without a decision behind it, or counting an approval the version
in force does not support.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
