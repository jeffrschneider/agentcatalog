---
name: cost-against-the-budget
description: Works out the labor cost of a plan, a position or an option from the pay range for each level, with benefits and the employer's taxes on pay, and sets it beside the budget for the finance lead to check. Use it when running `ref/hr/change-the-organization-structure` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: workforce-planner
  agent-version: "1"
---

# Cost against the budget

## What it does

Works out the labor cost of a plan, a position or an option from the pay
range for each level, with benefits and the employer's taxes on pay, and
sets it beside the budget for the finance lead to check.

## Where it happens

The agent does this in seven activities across four reference processes.
Each one names the activity as that process words it.

- **Check the Budget**
  - `ref/hr/open-a-position`, activity 8 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Check the Plan against the Budget**
  - `ref/hr/plan-the-workforce`, activity 9 -
    [Plan the Workforce](../../../../processes/human-resources/plan-the-workforce.md)
- **Cost Each Option**
  - `ref/hr/change-the-organization-structure`, activity 5 -
    [Change the Organization Structure](../../../../processes/human-resources/change-the-organization-structure.md)
- **Cost the Plan**
  - `ref/hr/plan-the-workforce`, activity 8 -
    [Plan the Workforce](../../../../processes/human-resources/plan-the-workforce.md)
- **Cost the Position**
  - `ref/hr/open-a-position`, activity 7 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Model the Options**
  - `ref/hr/run-a-layoff`, activity 2 -
    [Run a Layoff](../../../../processes/human-resources/run-a-layoff.md)
- **Write Down the Business Reason**
  - `ref/hr/run-a-layoff`, activity 1 -
    [Run a Layoff](../../../../processes/human-resources/run-a-layoff.md)

## What to record

A workforce plan leaves the business plan and the budget it was built
from at their versions, each department head's requests tied to a
target, the skill gaps named by team, each team's positions, levels,
start dates and labor cost, the cost set beside the budget with the name
of who checked it, the options with what each one gives up, the plan
published at a version with the decision and the approval that chose it,
and the assumptions the next plan checks first. A position request
leaves the request as it arrived, each gap sent back, the plan reading,
the cost for the rest of the year and a full year, the position marked
inside or outside the plan and the budget, any trade the department head
proposed, and the signed position on the plan with its level, range,
budget line and the names of those who signed. A reorganization leaves
the structure as it stood, each option with its reporting lines, its
cost and its one-time cost, and the effect of each option on every role,
all under the access list the head of HR set. A layoff leaves the labor
cost behind the business reason, each option with its cost, timing and
the number of people it affects, the roles in each pool with no names
attached, and the open positions offered to each selected person. Each
period leaves every figure beside the plan with its gap and each gap
handed to the plan's owner. Nothing in the record shows this agent
approving a plan or a position, or deciding about a person.

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
