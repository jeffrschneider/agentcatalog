---
name: control-what-is-out-to-sign
description: Sends the right version to the named signers in the agreed order, and takes a document back out of signature when it should no longer be out there, such as when the deal is lost. Use it when running `ref/sls/record-a-lost-deal` and `ref/sls/run-the-close-plan`.
license: CC-BY-4.0
metadata:
  agent: signature-manager
  agent-version: "1"
---

# Control what is out to sign

## What it does

Sends the right version to the named signers in the agreed order, and
takes a document back out of signature when it should no longer be out
there, such as when the deal is lost. The signing itself stays a human
step.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Execute the Signature**
  - `ref/sls/run-the-close-plan`, activity 15 -
    [Run the Close Plan](../../../../processes/sales/run-the-close-plan.md)
- **Stop the Open Work**
  - `ref/sls/record-a-lost-deal`, activity 9 -
    [Record a Lost Deal](../../../../processes/sales/record-a-lost-deal.md)

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
