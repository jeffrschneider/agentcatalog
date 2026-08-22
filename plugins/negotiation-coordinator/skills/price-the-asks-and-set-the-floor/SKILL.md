---
name: price-the-asks-and-set-the-floor
description: Sets the floor on price, term, liability and payment, and names who set it. Use it when running `ref/sls/negotiate-the-agreement`.
license: CC-BY-4.0
metadata:
  agent: negotiation-coordinator
  agent-version: "1"
---

# Price the asks and set the floor

## What it does

Sets the floor on price, term, liability and payment, and names who set
it. Prices each ask against what it costs and what it does to margin,
then sorts the list into give, trade and refuse, with what is asked for
in return on every trade.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Price the Asks**
  - `ref/sls/negotiate-the-agreement`, activity 5 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)
- **Set the Walk-Away Terms**
  - `ref/sls/negotiate-the-agreement`, activity 4 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)
- **Sort the Asks**
  - `ref/sls/negotiate-the-agreement`, activity 6 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)

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
