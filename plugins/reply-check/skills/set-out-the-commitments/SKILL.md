---
name: set-out-the-commitments
description: Sets out line by line what a held reply commits the company to, such as the fault, the date, the money and any change to the contract, and checks that any money offered was already decided by a named person who did not propose it. Use it when running `ref/sup/approve-a-sensitive-reply`.
license: CC-BY-4.0
metadata:
  agent: reply-check
  agent-version: "1"
---

# Set out the commitments

## What it does

Sets out line by line what a held reply commits the company to, such as
the fault, the date, the money and any change to the contract, and
checks that any money offered was already decided by a named person who
did not propose it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check the Money Was Decided**
  - `ref/sup/approve-a-sensitive-reply`, activity 7 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)
- **Set Out What the Reply Commits To**
  - `ref/sup/approve-a-sensitive-reply`, activity 6 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)

## What to record

Each check leaves the reply at the version checked, each sentence traced
to the content, the fact or the review it rests on, each sentence that
rests on none named, the rules read at their version, and whether the
reply was cleared or held. Each held reply leaves the rule that held it,
the named approver for its category and the one behind them, the case
set beside it, each commitment it makes with the fact or the decision
behind it, the refund or credit decision any money in it was matched to,
any legal matter or reporter's question passed on with the time, and
each changed version checked again with any new commitment named. Each
saved reply leaves its checks against its content and the reply rules
and, where it falls in a held category, the mark that sends it through
Approve a Sensitive Reply each time it is used. Each period leaves the
replies held without need, the replies changed and why, the matters sent
to the legal team, how long each held reply waited, and each rule that
missed a reply. Nothing in the record shows this agent approving or
sending a reply in a held category, rewording or splitting a held reply
to bring it out of its category, or offering money no named person had
decided.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
