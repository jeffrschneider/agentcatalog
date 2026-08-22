---
name: work-a-referral-into-the-list
description: Takes in an introduction somebody offers, reads the person and the account before anybody writes to them, and agrees with the seller what the introduction should ask for. Use it when running `ref/sls/work-a-referral`.
license: CC-BY-4.0
metadata:
  agent: prospect-researcher
  agent-version: "1"
---

# Work a referral into the list

## What it does

Takes in an introduction somebody offers, reads the person and the
account before anybody writes to them, and agrees with the seller what
the introduction should ask for. Records who introduces well and what
came of it.

## Where it happens

The agent does this in four activities across one reference process.
Each one names the activity as that process words it.

- **Agree What Is Being Asked**
  - `ref/sls/work-a-referral`, activity 5 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)
- **Read the Person and the Account**
  - `ref/sls/work-a-referral`, activity 4 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)
- **Record the Referral**
  - `ref/sls/work-a-referral`, activity 14 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)
- **Take in the Referral**
  - `ref/sls/work-a-referral`, activity 1 -
    [Work a Referral](../../../../processes/sales/work-a-referral.md)

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
