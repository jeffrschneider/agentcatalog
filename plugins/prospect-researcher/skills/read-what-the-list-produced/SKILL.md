---
name: read-what-the-list-produced
description: "Reads what the work produced: whether an account goes forward after the first conversation, and which fit rules found real prospects and which found noise. Use it when running `ref/sls/book-the-meeting` and `ref/sls/build-a-prospect-list`."
license: CC-BY-4.0
metadata:
  agent: prospect-researcher
  agent-version: "1"
---

# Read what the list produced

## What it does

Reads what the work produced: whether an account goes forward after the
first conversation, and which fit rules found real prospects and which
found noise.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Decide If It Goes Forward**
  - `ref/sls/book-the-meeting`, activity 12 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
- **Record What Was Learned**
  - `ref/sls/book-the-meeting`, activity 16 -
    [Book the Meeting](../../../../processes/sales/book-the-meeting.md)
  - `ref/sls/build-a-prospect-list`, activity 14 -
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
