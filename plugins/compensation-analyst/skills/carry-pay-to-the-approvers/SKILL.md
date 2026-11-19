---
name: carry-pay-to-the-approvers
description: Takes in a request for a pay change and checks it carries the reason, the evidence and the approvals the policy asks for, prepares the pay part of a promotion panel's pack, carries each proposed figure to the named approvers with the decision it rests on, and hands each approved promotion on to the record. Use it when running `ref/hr/change-an-employees-pay`, `ref/hr/decide-promotions` and `ref/hr/move-an-employee-to-a-new-role`.
license: CC-BY-4.0
metadata:
  agent: compensation-analyst
  agent-version: "1"
---

# Carry pay to the approvers

## What it does

Takes in a request for a pay change and checks it carries the reason,
the evidence and the approvals the policy asks for, prepares the pay
part of a promotion panel's pack, carries each proposed figure to the
named approvers with the decision it rests on, and hands each approved
promotion on to the record.

## Where it happens

The agent does this in six activities across three reference processes.
Each one names the activity as that process words it.

- **Check the Request Is Complete**
  - `ref/hr/change-an-employees-pay`, activity 2 -
    [Change an Employee's Pay](../../../../processes/human-resources/change-an-employees-pay.md)
- **Get the Pay Approved**
  - `ref/hr/move-an-employee-to-a-new-role`, activity 12 -
    [Move an Employee to a New Role](../../../../processes/human-resources/move-an-employee-to-a-new-role.md)
- **Get the Pay Changes Approved**
  - `ref/hr/decide-promotions`, activity 12 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Hand On Each Promotion**
  - `ref/hr/decide-promotions`, activity 16 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Prepare the Panel Pack**
  - `ref/hr/decide-promotions`, activity 7 -
    [Decide Promotions](../../../../processes/human-resources/decide-promotions.md)
- **Take in the Request**
  - `ref/hr/change-an-employees-pay`, activity 1 -
    [Change an Employee's Pay](../../../../processes/human-resources/change-an-employees-pay.md)

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
