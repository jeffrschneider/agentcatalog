---
name: stop-the-work-when-a-deal-ends
description: Stops the open contract work when a deal is called lost, so nothing is left pending against a buyer who is no longer buying. Use it when running `ref/sls/record-a-lost-deal`.
license: CC-BY-4.0
metadata:
  agent: redline-reviewer
  agent-version: "1"
---

# Stop the work when a deal ends

## What it does

Stops the open contract work when a deal is called lost, so nothing is
left pending against a buyer who is no longer buying.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Stop the Open Work**
  - `ref/sls/record-a-lost-deal`, activity 9 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)

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
