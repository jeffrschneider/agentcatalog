---
name: set-out-the-case-history
description: Reads the employee's warnings still in force, gathers the record behind a proposed dismissal, sets out the outcomes of similar past cases with the names withheld, and sets an outcome beside them for the consistency check. Use it when running `ref/hr/dismiss-an-employee` and `ref/hr/issue-a-disciplinary-action`.
license: CC-BY-4.0
metadata:
  agent: employee-case-keeper
  agent-version: "1"
---

# Set out the case history

## What it does

Reads the employee's warnings still in force, gathers the record behind
a proposed dismissal, sets out the outcomes of similar past cases with
the names withheld, and sets an outcome beside them for the consistency
check. It passes on any open concern, leave or accommodation only as the
fact that it is open and its dates.

## Where it happens

The agent does this in six activities across two reference processes.
Each one names the activity as that process words it.

- **Check for Open Matters**
  - `ref/hr/dismiss-an-employee`, activity 5 -
    [Dismiss an Employee](../../../../processes/human-resources/dismiss-an-employee.md)
- **Check the Outcome for Consistency**
  - `ref/hr/issue-a-disciplinary-action`, activity 11 -
    [Issue a Disciplinary Action](../../../../processes/human-resources/issue-a-disciplinary-action.md)
- **Compare with Similar Past Cases**
  - `ref/hr/dismiss-an-employee`, activity 4 -
    [Dismiss an Employee](../../../../processes/human-resources/dismiss-an-employee.md)
- **Gather the Record**
  - `ref/hr/dismiss-an-employee`, activity 2 -
    [Dismiss an Employee](../../../../processes/human-resources/dismiss-an-employee.md)
- **Read the Employee's Live Warnings**
  - `ref/hr/issue-a-disciplinary-action`, activity 4 -
    [Issue a Disciplinary Action](../../../../processes/human-resources/issue-a-disciplinary-action.md)
- **Set Out Similar Past Cases**
  - `ref/hr/issue-a-disciplinary-action`, activity 5 -
    [Issue a Disciplinary Action](../../../../processes/human-resources/issue-a-disciplinary-action.md)

## What to record

Each case leaves the concern, matter or referral as it was logged, with
its channel, its date, what it describes and whom it names, and an
anonymous concern under its case reference alone. It leaves the
acknowledgment with the date an answer was due, the restricted file with
every opening logged, the route with the person who chose it, the
hearing notes as the employee checked them, the written answer or
outcome with its reasons and the policy version it rests on, and any
appeal decision with the person who decided it. A disciplinary case also
leaves the employee's warnings still in force, the similar past cases
matched on the conduct, the clause and the circumstances `<your
disciplinary policy>` names and set out with the names withheld, the
consistency check with any difference explained in writing, and the date
the outcome stops counting with its reminder, and nothing reaches the
employee's wider record beyond what `<your disciplinary policy>` sets. A
plan leaves the plan at a version with the employee's comments, each
check-in note shared with the employee, the outcome with its reasons and
the person who decided it, and the review record told only that a plan
ran and how it ended. A dismissal case leaves the record the proposal
rests on, the like cases compared with the names taken out, each open
matter as the fact that it is open and its dates, and any appeal. Each
case closes with the date its file is to be destroyed under `<your
records retention schedule>`. Nothing in the record shows this agent
choosing a route, deciding an answer or an outcome, or finding out who
raised an anonymous concern.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
