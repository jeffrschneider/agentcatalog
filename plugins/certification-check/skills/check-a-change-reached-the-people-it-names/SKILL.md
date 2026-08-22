---
name: check-a-change-reached-the-people-it-names
description: Calls the roll against the list of who must be told, and runs the short check that the change is actually understood by the people who sat through it. Use it when running `ref/rev/roll-out-a-change`.
license: CC-BY-4.0
metadata:
  agent: certification-check
  agent-version: "1"
---

# Check a change reached the people it names

## What it does

Calls the roll against the list of who must be told, and runs the short
check that the change is actually understood by the people who sat
through it.

## Where it happens

The agent does this in two activities across one reference process. Each
one names the activity as that process words it.

- **Check That It Landed**
  - `ref/rev/roll-out-a-change`, activity 14 -
    [Roll Out a Change](../../../../processes/revenue-operations/roll-out-a-change.md)
- **Check Who Attended**
  - `ref/rev/roll-out-a-change`, activity 13 -
    [Roll Out a Change](../../../../processes/revenue-operations/roll-out-a-change.md)

## What to record

Per person: the request, naming who is put forward, for which job and by
when. The parts that must be proved, each with the reason a customer
would notice it. The assessment as checked, item by item, each item
naming the part of the standard it tests, and every item removed with
the reason. The assessors, and the conflicts that were ruled out. What
the assessors were briefed on, at a version. The sitting as scheduled,
including what the person was told they may bring. A score per part,
with the evidence it was given on and the assessor who gave it, kept so
a disputed score can be reread rather than re-argued. A score set aside
for conflict is kept marked as set aside, never deleted. The signed
result, who signed it, what it covers, and the condition and expiry on
any conditional pass. The certificate with its issue date, requirement
version and expiry. Attendance by name against the list of who must be
told. The later report setting scores against what those people did.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
