---
name: assess-the-customer
description: Takes in each request, identifies the legal entity that will be billed with any parent or guarantor, reads how it has paid the company before, and reads the risk against the credit policy to a rating with the rule behind each part. Use it when running `ref/fin/set-a-customers-credit-limit`.
license: CC-BY-4.0
metadata:
  agent: credit-analyst
  agent-version: "1"
---

# Assess the customer

## What it does

Takes in each request, identifies the legal entity that will be billed
with any parent or guarantor, reads how it has paid the company before,
and reads the risk against the credit policy to a rating with the rule
behind each part.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Identify the Entity That Will Be Billed**
  - `ref/fin/set-a-customers-credit-limit`, activity 2 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)
- **Read How the Customer Has Paid**
  - `ref/fin/set-a-customers-credit-limit`, activity 3 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)
- **Read the Risk Against the Credit Policy**
  - `ref/fin/set-a-customers-credit-limit`, activity 5 -
    [Set a Customer's Credit Limit](../../../../processes/finance/set-a-customers-credit-limit.md)
- **Take In the Request**
  - `ref/fin/set-a-customers-credit-limit`, activity 1 -
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
