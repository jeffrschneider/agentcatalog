---
name: set-the-rules-a-list-is-built-to
description: Takes in the territory or the approved plan a list is built from, and writes the fit rules down before anything is pulled. Use it when running `ref/sls/build-a-prospect-list`.
license: CC-BY-4.0
metadata:
  agent: prospect-researcher
  agent-version: "1"
---

# Set the rules a list is built to

## What it does

Takes in the territory or the approved plan a list is built from, and
writes the fit rules down before anything is pulled. The rules are
written plain enough for another person to apply them without asking.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Set the Fit Rules**
  - `ref/sls/build-a-prospect-list`, activity 2 -
    [Build a Prospect List](../../../../processes/sales/build-a-prospect-list.md)
- **Take in the Territory or Plan**
  - `ref/sls/build-a-prospect-list`, activity 1 -
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
