---
name: check-each-approval
description: Checks each approval against the version in force before it counts, and holds any approval by someone the version does not name, by an approver past their limit, or by the person who prepared or asked for the item, and reads each limit a finance policy names against the delegation. Use it when running `ref/fin/approve-an-investment-case` and 6 other reference processes.
license: CC-BY-4.0
metadata:
  agent: delegation-keeper
  agent-version: "1"
---

# Check each approval

## What it does

Checks each approval against the version in force before it counts, and
holds any approval by someone the version does not name, by an approver
past their limit, or by the person who prepared or asked for the item,
and reads each limit a finance policy names against the delegation.

## Where it happens

The agent does this in six activities across seven reference processes.
Each one names the activity as that process words it.

- **Check Each Approval Counts**
  - `ref/fin/issue-a-purchase-order`, activity 9 -
    [Issue a Purchase Order](../../../../processes/finance/issue-a-purchase-order.md)
- **Check Every Limit Against the Delegation**
  - `ref/fin/publish-a-finance-policy`, activity 7 -
    [Publish a Finance Policy](../../../../processes/finance/publish-a-finance-policy.md)
- **Check the Approval Counts**
  - `ref/fin/set-a-customers-credit-limit`, activity 10 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)
- **Check the Approval against the Delegation**
  - `ref/fin/approve-an-investment-case`, activity 14 -
    [Approve an Investment Case](../../../../processes/finance/approve-an-investment-case.md)
- **Check the Decision Counts**
  - `ref/sup/decide-a-refund-request`, activity 9 -
    [Decide a Refund Request](../../../../processes/customer-support/decide-a-refund-request.md)
  - `ref/sup/offer-a-goodwill-credit`, activity 8 -
    [Offer a Goodwill Credit](../../../../processes/customer-support/offer-a-goodwill-credit.md)
- **Confirm Each Approval Counts**
  - `ref/fin/post-a-manual-journal-entry`, activity 9 -
    [Post a Manual Journal Entry](../../../../processes/finance/post-a-manual-journal-entry.md)

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
