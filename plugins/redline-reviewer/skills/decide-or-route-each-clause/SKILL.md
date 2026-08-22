---
name: decide-or-route-each-clause
description: Sends the clauses only a lawyer may answer to a named lawyer, and closes the rest as accept, counter or reject, each with its reason and the person who made the decision. Use it when running `ref/sls/review-the-redlines`.
license: CC-BY-4.0
metadata:
  agent: redline-reviewer
  agent-version: "1"
---

# Decide or route each clause

## What it does

Sends the clauses only a lawyer may answer to a named lawyer, and closes
the rest as accept, counter or reject, each with its reason and the
person who made the decision.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Decide Each Clause**
  - `ref/sls/review-the-redlines`, activity 9 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)
- **Route the Clauses Only Legal Answers**
  - `ref/sls/review-the-redlines`, activity 8 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)

## What to record

Per review: the markup at its version and the copy it was made from. One
item per changed clause, with the original text and the buyer's text
side by side, its class, and its clause number. What was decided on the
same change in past deals and who decided it. Every clause closed as
accept, counter or reject, each with its reason and the person who made
the decision. The counter-markup with every off-template term listed
separately and every approver named. The version sent back and the date.
Each further markup read against the copy we last sent, with every
difference named. The confirmed clean text, and the accepted changes
written to the record other deals read.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
