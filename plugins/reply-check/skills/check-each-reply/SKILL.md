---
name: check-each-reply
description: Reads each drafted reply, complaint answer, outage summary, reply to a reporter and saved reply against the content it cites, the facts or the record it rests on and the reply rules at their version, names any sentence that rests on none of them, and checks a changed reply again. Use it when running `ref/sup/answer-a-formal-complaint` and 5 other reference processes.
license: CC-BY-4.0
metadata:
  agent: reply-check
  agent-version: "1"
---

# Check each reply

## What it does

Reads each drafted reply, complaint answer, outage summary, reply to a
reporter and saved reply against the content it cites, the facts or the
record it rests on and the reply rules at their version, names any
sentence that rests on none of them, and checks a changed reply again.

## Where it happens

The agent does this in seven activities across six reference processes.
Each one names the activity as that process words it.

- **Check a Changed Reply Again**
  - `ref/sup/approve-a-sensitive-reply`, activity 10 -
    [Approve a Sensitive Reply](../../../../processes/customer-support/approve-a-sensitive-reply.md)
- **Check the Answer**
  - `ref/sup/answer-a-formal-complaint`, activity 13 -
    [Answer a Formal Complaint](../../../../processes/customer-support/answer-a-formal-complaint.md)
- **Check the Reply**
  - `ref/sup/escalate-a-security-or-safety-report`, activity 10 -
    [Escalate a Security or Safety Report](../../../../processes/customer-support/escalate-a-security-or-safety-report.md)
- **Check the Reply Against Its Content**
  - `ref/sup/publish-a-saved-reply`, activity 7 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Check the Reply Against the Reply Rules**
  - `ref/sup/publish-a-saved-reply`, activity 8 -
    [Publish a Saved Reply](../../../../processes/customer-support/publish-a-saved-reply.md)
- **Check the Reply Before It Goes**
  - `ref/sup/resolve-a-case`, activity 6 -
    [Resolve a Case](../../../../processes/customer-support/resolve-a-case.md)
- **Check the Summary**
  - `ref/sup/follow-up-an-outage`, activity 6 -
    [Follow Up an Outage](../../../../processes/customer-support/follow-up-an-outage.md)

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
