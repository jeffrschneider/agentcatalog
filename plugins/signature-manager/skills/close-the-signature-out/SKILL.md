---
name: close-the-signature-out
description: Puts one booking in front of everybody who acts on it at the same time, so nobody works from an older version of what was signed. Use it when running `ref/sls/book-the-order`.
license: CC-BY-4.0
metadata:
  agent: signature-manager
  agent-version: "1"
---

# Close the signature out

## What it does

Puts one booking in front of everybody who acts on it at the same time,
so nobody works from an older version of what was signed. Writes down
what had to be corrected between signature and booking, and which of it
belongs in the next version of the paper.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Record What Had to Be Fixed**
  - `ref/sls/book-the-order`, activity 16 -
    [Book the Order](../../../../processes/sales/book-the-order.md)
- **Tell the People Who Need to Know**
  - `ref/sls/book-the-order`, activity 15 -
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
