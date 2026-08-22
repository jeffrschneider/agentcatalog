---
name: answer-the-commercial-terms-in-a-markup
description: Reads the price, term and scope changes inside a buyer's markup, because a commercial ask dressed as a legal change is settled here rather than inside the contract text. Use it when running `ref/sls/review-the-redlines`.
license: CC-BY-4.0
metadata:
  agent: negotiation-coordinator
  agent-version: "1"
---

# Answer the commercial terms in a markup

## What it does

Reads the price, term and scope changes inside a buyer's markup, because
a commercial ask dressed as a legal change is settled here rather than
inside the contract text.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Review the Business Terms**
  - `ref/sls/review-the-redlines`, activity 6 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)

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
