---
name: keep-the-customer-under-review
description: Sets the next review date and the warning signs to watch, sets the follow-up level for collections and gives it when an invoice is overdue, reviews the customer's credit when a promise is broken or a debt grows, and records what each review taught. Use it when running `ref/fin/collect-an-overdue-invoice` and `ref/fin/set-a-customers-credit-limit`.
license: CC-BY-4.0
metadata:
  agent: credit-analyst
  agent-version: "1"
---

# Keep the customer under review

## What it does

Sets the next review date and the warning signs to watch, sets the
follow-up level for collections and gives it when an invoice is overdue,
reviews the customer's credit when a promise is broken or a debt grows,
and records what each review taught.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Read the Follow-Up Level**
  - `ref/fin/collect-an-overdue-invoice`, activity 3 -
    [Collect an Overdue Invoice](../../../../processes/finance/collect-an-overdue-invoice.md)
- **Record What the Review Taught**
  - `ref/fin/set-a-customers-credit-limit`, activity 16 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)
- **Review the Customer's Credit**
  - `ref/fin/collect-an-overdue-invoice`, activity 10 -
    [Collect an Overdue Invoice](../../../../processes/finance/collect-an-overdue-invoice.md)
- **Set the Follow-Up Level for Collections**
  - `ref/fin/set-a-customers-credit-limit`, activity 15 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)
- **Set the Review Date**
  - `ref/fin/set-a-customers-credit-limit`, activity 14 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)

## What to record

Each credit run leaves what opened it, the legal entity that will be
billed with any parent or guarantor, the payment history with its dates,
the reports and filings with their sources and the dates they were read,
the rating with the policy rule and version behind each part, and any
part the evidence cannot support named as unsupported. Beside them sit
the proposed limit, terms and security with the evidence behind each
figure, the account owner's view, the approver's decision as recorded,
the review date with the warning signs to watch, and the follow-up level
passed to collections. Each review during collection leaves what opened
it and what it found. Nothing in the record shows this agent setting,
recording or changing a limit, or holding an order.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
