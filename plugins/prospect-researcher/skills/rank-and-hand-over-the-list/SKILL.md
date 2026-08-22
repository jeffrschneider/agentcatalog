---
name: rank-and-hand-over-the-list
description: Ranks the list so the seller knows what to work first, takes the seller's keeps, drops and adds with a reason against each, and loads the signed list where the sequences read it. Use it when running `ref/sls/build-a-prospect-list`.
license: CC-BY-4.0
metadata:
  agent: prospect-researcher
  agent-version: "1"
---

# Rank and hand over the list

## What it does

Ranks the list so the seller knows what to work first, takes the
seller's keeps, drops and adds with a reason against each, and loads the
signed list where the sequences read it. Sets the date the list is built
again and the triggers that force it earlier.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Load the List**
  - `ref/sls/build-a-prospect-list`, activity 12 -
    [Build a Prospect List](../../../../processes/sales/build-a-prospect-list.md)
- **Review with the Seller**
  - `ref/sls/build-a-prospect-list`, activity 10 -
    [Build a Prospect List](../../../../processes/sales/build-a-prospect-list.md)
- **Score and Rank**
  - `ref/sls/build-a-prospect-list`, activity 9 -
    [Build a Prospect List](../../../../processes/sales/build-a-prospect-list.md)
- **Set the Refresh**
  - `ref/sls/build-a-prospect-list`, activity 13 -
    [Build a Prospect List](../../../../processes/sales/build-a-prospect-list.md)

## What to record

The fit rules as written, at a version, plain enough for another person
to apply without asking. Per person: the account and the role, the
source they came from, the date they were pulled, the verification
result kept apart from the details that failed, and the consent finding
channel by channel with the count the record took out. Per list: the
rank with the inputs and the model version behind it, a reason against
every account the seller dropped or added, the signature with the signer
and the date, the loaded list as it reached the CRM and the sending
system, and the rebuild date with the triggers that force a rebuild
earlier.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
