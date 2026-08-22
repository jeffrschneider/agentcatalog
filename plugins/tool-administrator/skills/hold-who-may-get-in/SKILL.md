---
name: hold-who-may-get-in
description: Sets the roles and what each one may do, opens an account against a job and closes it against a leaving record, and reads every account again on its cadence. Use it when running `ref/rev/administer-a-tool`.
license: CC-BY-4.0
metadata:
  agent: tool-administrator
  agent-version: "1"
---

# Hold who may get in

## What it does

Sets the roles and what each one may do, opens an account against a job
and closes it against a leaving record, and reads every account again on
its cadence. A leaver who kept an account and an account nobody can
account for both go to the security reviewer.

## Where it happens

The agent does this in three activities across one reference process.
Each one names the activity as that process words it.

- **Open and Close Accounts**
  - `ref/rev/administer-a-tool`, activity 3 -
    [Administer a Tool](../../../../processes/revenue-operations/administer-a-tool.md)
- **Read Every Account Again**
  - `ref/rev/administer-a-tool`, activity 12 -
    [Administer a Tool](../../../../processes/revenue-operations/administer-a-tool.md)
- **Set the Roles and the Permissions**
  - `ref/rev/administer-a-tool`, activity 2 -
    [Administer a Tool](../../../../processes/revenue-operations/administer-a-tool.md)

## What to record

The entry as it was taken on: the owner, the licence, the term and the
process the tool runs. Every account open today with its role and its
named approver, and every closure with its date and how long the account
stood after the leaving record. The configuration at a version, each
change carrying its date, the request behind it, what the trial away
from live showed, and the way back that was kept. Each licence count
setting licences paid for against licences used, naming every licence
unused past the limit. Every refused request, with the reason and the
process it belongs to. The review recorded with its decision, its date,
the evidence it was made on and the date the next one falls. In a
retirement: who was told and when, the export with everything the tool
held that it could not take, every link stopped with what it was
carrying, the read-only date, the closed accounts, the notice given and
the final invoice.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
