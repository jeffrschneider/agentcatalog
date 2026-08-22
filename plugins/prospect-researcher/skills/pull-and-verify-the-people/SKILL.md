---
name: pull-and-verify-the-people
description: Pulls the accounts that meet the rules, finds the roles worth approaching at each one, and checks every address and number against a source before it is used. Use it when running `ref/sls/build-a-prospect-list`.
license: CC-BY-4.0
metadata:
  agent: prospect-researcher
  agent-version: "1"
---

# Pull and verify the people

## What it does

Pulls the accounts that meet the rules, finds the roles worth
approaching at each one, and checks every address and number against a
source before it is used. Each person carries where they came from and
the date they were pulled.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Find the People**
  - `ref/sls/build-a-prospect-list`, activity 6 -
    [Build a Prospect List](../../../../processes/sales/build-a-prospect-list.md)
- **Pull the Candidate Accounts**
  - `ref/sls/build-a-prospect-list`, activity 3 -
    [Build a Prospect List](../../../../processes/sales/build-a-prospect-list.md)
- **Verify the Contact Details**
  - `ref/sls/build-a-prospect-list`, activity 7 -
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
