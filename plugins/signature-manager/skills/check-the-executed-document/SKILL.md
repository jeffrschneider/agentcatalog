---
name: check-the-executed-document
description: Takes the executed copy in with every exhibit it names, and confirms who signed on each side, under what authority, and on what date. Use it when running `ref/sls/book-the-order`.
license: CC-BY-4.0
metadata:
  agent: signature-manager
  agent-version: "1"
---

# Check the executed document

## What it does

Takes the executed copy in with every exhibit it names, and confirms who
signed on each side, under what authority, and on what date. An exhibit
that is not there is named as missing rather than assumed.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Confirm the Signature and the Signer**
  - `ref/sls/book-the-order`, activity 2 -
    [Book the Order](../../../../processes/sales/book-the-order.md)
- **Take in the Executed Agreement**
  - `ref/sls/book-the-order`, activity 1 -
    [Book the Order](../../../../processes/sales/book-the-order.md)

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
