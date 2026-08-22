---
name: mark-which-promises-the-paper-carries
description: Reads the promises made during the sale against the executed text and marks each one carried by the agreement, carried by a side letter, or said and not binding. Use it when running `ref/sls/hand-over-to-delivery`.
license: CC-BY-4.0
metadata:
  agent: signature-manager
  agent-version: "1"
---

# Mark which promises the paper carries

## What it does

Reads the promises made during the sale against the executed text and
marks each one carried by the agreement, carried by a side letter, or
said and not binding. Every binding one names the clause behind it.

## Where it happens

The agent does this in one activity across one reference process. Each
one names the activity as that process words it.

- **Separate the Contract from the Conversation**
  - `ref/sls/hand-over-to-delivery`, activity 6 -
    [Hand over to Delivery](../../../../processes/sales/hand-over-to-delivery.md)

## What to record

Per agreement: the executed document at a version, with each exhibit it
names marked present or missing. The signers on both sides, the
authority each signed under, and the signature date the term runs from.
The buying entity and the selling entity as matched to the entity list,
with the tax and address record for each. Every term off the standard
paper, named as non-standard, with the person who accepted it and the
date. Each promise made during the sale marked binding, carried by a
side letter, or not binding, with the clause behind every binding one.
The signature path as confirmed, and the date and version each document
went out on. What had to be corrected between signature and booking, and
which of it belongs in the next version of the paper. Somebody auditing
a run can say which version was signed, by whom, and what it obliges.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
