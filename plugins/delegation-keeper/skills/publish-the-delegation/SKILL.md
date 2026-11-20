---
name: publish-the-delegation
description: Publishes the approved delegation at a version with its effective date, so every approval asked from that date reads it, and hands each change that another process carries out to that process's owner. Use it when running `ref/fin/publish-the-delegation-of-authority`.
license: CC-BY-4.0
metadata:
  agent: delegation-keeper
  agent-version: "1"
---

# Publish the delegation

## What it does

Publishes the approved delegation at a version with its effective date,
so every approval asked from that date reads it, and hands each change
that another process carries out to that process's owner.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Hand On the Changes Other Processes Make**
  - `ref/fin/publish-the-delegation-of-authority`, activity 14 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
- **Publish the Delegation at a Version**
  - `ref/fin/publish-the-delegation-of-authority`, activity 11 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)

## What to record

Each change leaves the reason behind it with the decision, the role
change, the finding or the review date on the record, the version in
force as it was read, how the approvals since it ran with each one sent
above its level, given by a stand-in, matching no line or stopped, each
version of the draft with every change marked and its stand-ins named,
the check for gaps and clashes with each line drafted again, counsel's
points, the approval by the board or the people it names, the version
published with its effective date, and each change handed to the owner
of the process that carries it out. In every other process each request
leaves the approvers and stand-ins named with the version they were read
from, and each approval checked as counting or held with the reason,
such as an approver the version does not name, an amount past the
approver's limit or an approval by the person who prepared the item.
Nothing in the record shows this agent approving an item, changing a
line without a decision behind it, or counting an approval the version
in force does not support.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
