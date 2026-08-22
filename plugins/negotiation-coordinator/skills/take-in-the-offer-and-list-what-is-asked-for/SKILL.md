---
name: take-in-the-offer-and-list-what-is-asked-for
description: Reads the offer as it was sent and the reply that came back, and gathers every ask into one numbered list in the buyer's own words with the person who raised each one. Use it when running `ref/sls/negotiate-the-agreement`.
license: CC-BY-4.0
metadata:
  agent: negotiation-coordinator
  agent-version: "1"
---

# Take in the offer and list what is asked for

## What it does

Reads the offer as it was sent and the reply that came back, and gathers
every ask into one numbered list in the buyer's own words with the
person who raised each one. Confirms who actually signs on each side and
who they need first.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Confirm Who Decides**
  - `ref/sls/negotiate-the-agreement`, activity 3 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)
- **List What Is Asked For**
  - `ref/sls/negotiate-the-agreement`, activity 2 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)
- **Take in the Offer and the Reply**
  - `ref/sls/negotiate-the-agreement`, activity 1 -
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
