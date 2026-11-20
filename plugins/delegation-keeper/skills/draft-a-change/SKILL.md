---
name: draft-a-change
description: Takes in the reason for a change with the decision behind it, reads the version in force and how the approvals since it ran against it, drafts the new lines with the CFO with every change marked, names a stand-in for every approver, and checks the draft so every kind of decision has an approver and nobody approves their own work. Use it when running `ref/fin/publish-the-delegation-of-authority`.
license: CC-BY-4.0
metadata:
  agent: delegation-keeper
  agent-version: "1"
---

# Draft a change

## What it does

Takes in the reason for a change with the decision behind it, reads the
version in force and how the approvals since it ran against it, drafts
the new lines with the CFO with every change marked, names a stand-in
for every approver, and checks the draft so every kind of decision has
an approver and nobody approves their own work.

## Where it happens

The agent does this in six activities across one reference process. Each
one names the activity as that process words it.

- **Check the Draft for Gaps and Clashes**
  - `ref/fin/publish-the-delegation-of-authority`, activity 7 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
- **Draft the Change**
  - `ref/fin/publish-the-delegation-of-authority`, activity 5 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
- **Name a Stand-In for Each Approver**
  - `ref/fin/publish-the-delegation-of-authority`, activity 6 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
- **Read How Approvals Ran**
  - `ref/fin/publish-the-delegation-of-authority`, activity 3 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
- **Read the Version in Force**
  - `ref/fin/publish-the-delegation-of-authority`, activity 2 -
    [Publish the Delegation of Authority](../../../../processes/finance/publish-the-delegation-of-authority.md)
- **Take in the Reason to Change**
  - `ref/fin/publish-the-delegation-of-authority`, activity 1 -
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
