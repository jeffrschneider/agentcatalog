---
name: hold-for-the-named-person
description: Holds a reply in a category a named person must send, names the rule and the approver for its category, marks a saved reply in such a category for approval each time it is used, holds each reply to a reporter or about a credit for the person who sends it, and passes a legal matter or a reporter's question to the team that must answer it. Use it when running `ref/sup/approve-a-sensitive-reply` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: reply-check
  agent-version: "1"
---

# Hold for the named person

## What it does

Holds a reply in a category a named person must send, names the rule and
the approver for its category, marks a saved reply in such a category
for approval each time it is used, holds each reply to a reporter or
about a credit for the person who sends it, and passes a legal matter or
a reporter's question to the team that must answer it.

## Where it happens

The agent does this in seven activities across five reference processes.
Each one names the activity as that process words it.

- **Hold a Sensitive Reply**
  - `ref/sup/resolve-a-case`, activity 7 -
    [Resolve a Case](../../../../processes/customer-support/resolve-a-case.md)
- **Mark It for Approval Each Time It Is Used**
  - `ref/sup/publish-a-saved-reply`, activity 9 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Name the Approver for Its Category**
  - `ref/sup/approve-a-sensitive-reply`, activity 2 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)
- **Pass What Another Team Must Answer**
  - `ref/sup/approve-a-sensitive-reply`, activity 5 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)
- **Take In the Held Reply**
  - `ref/sup/approve-a-sensitive-reply`, activity 1 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)
- **Tell Each Customer Its Credit**
  - `ref/sup/follow-up-an-outage`, activity 14 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)
- **Tell the Reporter the Outcome**
  - `ref/sup/escalate-a-security-or-safety-report`, activity 15 -
    [Escalate a Security or Safety Report](../../../../processes/customer-support/escalate-a-security-or-safety-report.md)

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
