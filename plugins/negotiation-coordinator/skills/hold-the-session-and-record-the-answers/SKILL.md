---
name: hold-the-session-and-record-the-answers
description: Runs the session against the sorted list, and closes each ask with its answer, its reason, its date and the name of the person on each side who agreed to it. Use it when running `ref/sls/negotiate-the-agreement`.
license: CC-BY-4.0
metadata:
  agent: negotiation-coordinator
  agent-version: "1"
---

# Hold the session and record the answers

## What it does

Runs the session against the sorted list, and closes each ask with its
answer, its reason, its date and the name of the person on each side who
agreed to it. A refusal goes back to the buyer in writing rather than
only in a call.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Hold the Negotiation Session**
  - `ref/sls/negotiate-the-agreement`, activity 8 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)
- **Record What Was Agreed**
  - `ref/sls/negotiate-the-agreement`, activity 9 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)
- **Refuse in Writing**
  - `ref/sls/negotiate-the-agreement`, activity 10 -
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
