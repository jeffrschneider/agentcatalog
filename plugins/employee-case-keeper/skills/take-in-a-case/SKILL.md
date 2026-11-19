---
name: take-in-a-case
description: Logs each concern, conduct matter and referral once, from any channel, named or anonymous, acknowledges a concern with the date an answer is due, and opens a restricted file or case that only the named people on it can open, logging every opening. Use it when running `ref/hr/investigate-a-workplace-complaint` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: employee-case-keeper
  agent-version: "1"
---

# Take in a case

## What it does

Logs each concern, conduct matter and referral once, from any channel,
named or anonymous, acknowledges a concern with the date an answer is
due, and opens a restricted file or case that only the named people on
it can open, logging every opening.

## Where it happens

The agent does this in six activities across four reference processes.
Each one names the activity as that process words it.

- **Acknowledge the Concern**
  - `ref/hr/resolve-an-employee-concern`, activity 2 -
    [Resolve an Employee Concern](../../../../processes/human-resources/resolve-an-employee-concern.md)
- **Open the Restricted Case**
  - `ref/hr/run-a-performance-improvement-plan`, activity 2 -
    [Run a Performance Improvement Plan](../../../../processes/human-resources/run-a-performance-improvement-plan.md)
- **Open the Restricted File**
  - `ref/hr/resolve-an-employee-concern`, activity 4 -
    [Resolve an Employee Concern](../../../../processes/human-resources/resolve-an-employee-concern.md)
- **Take in the Concern**
  - `ref/hr/resolve-an-employee-concern`, activity 1 -
    [Resolve an Employee Concern](../../../../processes/human-resources/resolve-an-employee-concern.md)
- **Take in the Conduct Matter**
  - `ref/hr/issue-a-disciplinary-action`, activity 1 -
    [Issue a Disciplinary Action](../../../../processes/human-resources/issue-a-disciplinary-action.md)
- **Take in the Referral**
  - `ref/hr/investigate-a-workplace-complaint`, activity 1 -
    [Investigate a Workplace Complaint](../../../../processes/human-resources/investigate-a-workplace-complaint.md)

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
