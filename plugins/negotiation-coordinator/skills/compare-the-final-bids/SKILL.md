---
name: compare-the-final-bids
description: Sets the final bids in a sale side by side on price, certainty of closing, financing, the promises asked of the sellers, escrow and timing, and on what each one pays the fund after the debt and the preferences, taking that last figure from the cap-table-keeper agent. Use it when running `ref/pc/run-a-sale-process`.
license: CC-BY-4.0
metadata:
  agent: negotiation-coordinator
  agent-version: "1"
---

# Compare the final bids

## What it does

Sets the final bids in a sale side by side on price, certainty of
closing, financing, the promises asked of the sellers, escrow and
timing, and on what each one pays the fund after the debt and the
preferences, taking that last figure from the cap-table-keeper agent.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Compare the Final Bids**
  - `ref/pc/run-a-sale-process`, activity 11 -
    [Run a Sale Process](../../../../processes/private-capital/run-a-sale-process.md)

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
