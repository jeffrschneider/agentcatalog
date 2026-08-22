---
name: build-the-check-of-what-was-taught
description: Builds the questions, the exercises and the scenarios a sitting uses, each item naming the part of the standard it tests, and the short check that a change was understood. Use it when running `ref/rev/certify-a-seller` and `ref/rev/roll-out-a-change`.
license: CC-BY-4.0
metadata:
  agent: curriculum-manager
  agent-version: "1"
---

# Build the check of what was taught

## What it does

Builds the questions, the exercises and the scenarios a sitting uses,
each item naming the part of the standard it tests, and the short check
that a change was understood. It builds these and never scores the
person taking them.

## Where it happens

The agent does this in two activities across two reference processes.
Each one names the activity as that process words it.

- **Build the Assessment**
  - `ref/rev/certify-a-seller`, activity 4 -
    [Certify a Seller](../../../../processes/revenue-operations/certify-a-seller.md)
- **Check That It Landed**
  - `ref/rev/roll-out-a-change`, activity 14 -
    [Roll Out a Change](../../../../processes/revenue-operations/roll-out-a-change.md)

## What to record

Per plan: what each role has to prove, written as testable lines at a
version, and every course traced to the requirement it covers. What each
person was excused, with the evidence behind the exemption. The
schedule, with who was expected in each session. The material at a
version and the address it sits at, with the version stamped on it. Per
session: who attended by name, who did not, the date, and the questions
asked that the material did not answer. Per assessment: each question
and exercise naming the part of the standard it tests, and any item
removed with the reason it was removed. Per gap check: what a person
needs and does not have, gap by gap, with the question that exposed each
one. Per retrain: the gap named, the date it was taught again, and who
sat it. Any change to a plan after teaching started, dated. Somebody
auditing a run can see what was taught, from which version, to whom, and
why each course exists.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
