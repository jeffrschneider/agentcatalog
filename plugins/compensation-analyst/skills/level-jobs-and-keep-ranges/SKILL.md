---
name: level-jobs-and-keep-ranges
description: Places a job at a level in the job framework by matching its duties and must-haves to the level descriptions, confirms the job and level a new figure is for, reads the range kept for each level and location, and refreshes every range from the market data in the pay review. Use it when running `ref/hr/change-an-employees-pay` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: compensation-analyst
  agent-version: "1"
---

# Level jobs and keep ranges

## What it does

Places a job at a level in the job framework by matching its duties and
must-haves to the level descriptions, confirms the job and level a new
figure is for, reads the range kept for each level and location, and
refreshes every range from the market data in the pay review.

## Where it happens

The agent does this in five activities across four reference processes.
Each one names the activity as that process words it.

- **Confirm the Job and Its Level**
  - `ref/hr/change-an-employees-pay`, activity 3 -
    [Change an Employee's Pay](../../../../processes/human-resources/change-an-employees-pay.md)
- **Confirm the Job at the Next Level**
  - `ref/hr/decide-promotions`, activity 5 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Place the Job at a Level**
  - `ref/hr/open-a-position`, activity 5 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Refresh the Pay Ranges**
  - `ref/hr/run-the-pay-review`, activity 3 -
    [Run the Pay Review](../../../../processes/human-resources/run-the-pay-review.md)
- **Set the Pay Range**
  - `ref/hr/open-a-position`, activity 6 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)

## What to record

Each job placed leaves the level it was matched to, the level
description it matched, the nearest jobs at that level and the range
read with the date of its market data. Each figure proposed leaves the
figure, where it sits in the range, the pay of people doing like work
beside it, the cost this year and in a full year against what is left in
the budget, the reason for each point, and any exception with the
approver it needs, beside the named approvers' decision and its date.
Each pay change request leaves the request as it arrived, what was
missing, the checks, the proposed figure and the decision brought back
to it. Each pay review leaves the ranges refreshed from the market data
with the change from last year and the people each would leave outside
it, the cost of each budget option, every manager's proposal checked
with each one outside the guidelines named and its reason attached, and
the spend against the budget. Each promotion round leaves the job
confirmed at the next level and the proposed pay for each promotion, the
spend against the round's budget, and each approved promotion handed on
to the record. Every range that keeps being breached is flagged with its
count for the next review. Nothing in the record shows this agent
approving a range or a pay decision, or reading a protected
characteristic.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
