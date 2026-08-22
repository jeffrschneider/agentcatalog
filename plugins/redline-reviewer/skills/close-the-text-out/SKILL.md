---
name: close-the-text-out
description: Reads the agreed commercial position against the paper term by term, settles one clean text both sides call the agreement, checks that every condition owed before signature is done, and writes the accepted changes to the record the next deal reads. Use it when running `ref/sls/negotiate-the-agreement`, `ref/sls/review-the-redlines` and `ref/sls/run-the-close-plan`.
license: CC-BY-4.0
metadata:
  agent: redline-reviewer
  agent-version: "1"
---

# Close the text out

## What it does

Reads the agreed commercial position against the paper term by term,
settles one clean text both sides call the agreement, checks that every
condition owed before signature is done, and writes the accepted changes
to the record the next deal reads.

## Where it happens

The agent does this in four activities across three reference processes.
Each one names the activity as that process words it.

- **Confirm the Clean Copy**
  - `ref/sls/review-the-redlines`, activity 14 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)
- **Confirm the Close Conditions**
  - `ref/sls/run-the-close-plan`, activity 14 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Log the Clause Decisions**
  - `ref/sls/review-the-redlines`, activity 15 -
    [Review the Redlines](../../../../processes/sales/review-the-redlines.md)
- **Reconcile with the Contract Draft**
  - `ref/sls/negotiate-the-agreement`, activity 13 -
    [Negotiate the Agreement](../../../../processes/sales/negotiate-the-agreement.md)

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
