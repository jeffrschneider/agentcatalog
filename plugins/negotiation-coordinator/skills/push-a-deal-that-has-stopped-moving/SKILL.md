---
name: push-a-deal-that-has-stopped-moving
description: Takes a step nobody will move up on both sides, and makes one named attempt to reopen a deal that was called lost, with the answer recorded either way. Use it when running `ref/sls/record-a-lost-deal` and `ref/sls/run-the-close-plan`.
license: CC-BY-4.0
metadata:
  agent: negotiation-coordinator
  agent-version: "1"
---

# Push a deal that has stopped moving

## What it does

Takes a step nobody will move up on both sides, and makes one named
attempt to reopen a deal that was called lost, with the answer recorded
either way.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Escalate a Stalled Step**
  - `ref/sls/run-the-close-plan`, activity 13 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Make One Recovery Attempt**
  - `ref/sls/record-a-lost-deal`, activity 3 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)

## What to record

The numbered list of asks in the buyer's own wording, each with the
person who raised it. The floor on price, term, liability and payment,
and who set it. What each ask costs, which budget carries it, and the
margin after it. Each ask marked give, trade or refuse, with what was
asked for in return on every trade. Every approval with its approver and
its date, given before the concession was offered. Every closed ask with
the answer, the reason, the date and the person on each side who agreed.
Every refusal as it went to the buyer. The rebuilt offer with each
changed line traced to an ask, and the dated position both sides
confirmed, with the open items nobody closed listed beside it.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
