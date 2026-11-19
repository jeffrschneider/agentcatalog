---
name: close-the-case
description: Sets the date an outcome stops counting with its reminder, closes each case and investigation file under restricted access with its retention date, and adds what the case showed to the debrief. Use it when running `ref/hr/dismiss-an-employee` and 4 other reference processes.
license: CC-BY-4.0
metadata:
  agent: employee-case-keeper
  agent-version: "1"
---

# Close the case

## What it does

Sets the date an outcome stops counting with its reminder, closes each
case and investigation file under restricted access with its retention
date, and adds what the case showed to the debrief.

## Where it happens

The agent does this in five activities across five reference processes.
Each one names the activity as that process words it.

- **Close the Case**
  - `ref/hr/dismiss-an-employee`, activity 16 -
    [Dismiss an Employee](../../../../processes/human-resources/dismiss-an-employee.md)
  - `ref/hr/issue-a-disciplinary-action`, activity 17 -
    [Issue a Disciplinary Action](../../../../processes/human-resources/issue-a-disciplinary-action.md)
  - `ref/hr/resolve-an-employee-concern`, activity 16 -
    [Resolve an Employee Concern](../../../../processes/human-resources/resolve-an-employee-concern.md)
  - `ref/hr/run-a-performance-improvement-plan`, activity 16 -
    [Run a Performance Improvement Plan](../../../../processes/human-resources/run-a-performance-improvement-plan.md)
- **Close the Investigation File**
  - `ref/hr/investigate-a-workplace-complaint`, activity 18 -
    [Investigate a Workplace Complaint](../../../../processes/human-resources/investigate-a-workplace-complaint.md)
- **Record What the Case Taught**
  - `ref/hr/resolve-an-employee-concern`, activity 17 -
    [Resolve an Employee Concern](../../../../processes/human-resources/resolve-an-employee-concern.md)
- **Record What the Investigation Taught**
  - `ref/hr/investigate-a-workplace-complaint`, activity 19 -
    [Investigate a Workplace Complaint](../../../../processes/human-resources/investigate-a-workplace-complaint.md)
- **Set the Expiry Date**
  - `ref/hr/issue-a-disciplinary-action`, activity 16 -
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
