---
name: model-structure-changes
description: Draws the structure as it stands and the options for a reorganization, lists the effect of each option on every role, lists the roles in each selection pool of a layoff with no names attached, and finds the open positions a selected person could take. Use it when running `ref/hr/change-the-organization-structure` and `ref/hr/run-a-layoff`.
license: CC-BY-4.0
metadata:
  agent: workforce-planner
  agent-version: "1"
---

# Model structure changes

## What it does

Draws the structure as it stands and the options for a reorganization,
lists the effect of each option on every role, lists the roles in each
selection pool of a layoff with no names attached, and finds the open
positions a selected person could take.

## Where it happens

The agent does this in five activities across two reference processes.
Each one names the activity as that process words it.

- **Draw the Current Structure**
  - `ref/hr/change-the-organization-structure`, activity 3 -
    [Change the Organization Structure](../../../../processes/human-resources/change-the-organization-structure.md)
- **Draw the Options**
  - `ref/hr/change-the-organization-structure`, activity 4 -
    [Change the Organization Structure](../../../../processes/human-resources/change-the-organization-structure.md)
- **List the Effect on Each Role**
  - `ref/hr/change-the-organization-structure`, activity 6 -
    [Change the Organization Structure](../../../../processes/human-resources/change-the-organization-structure.md)
- **List the Roles Affected**
  - `ref/hr/run-a-layoff`, activity 4 -
    [Run a Layoff](../../../../processes/human-resources/run-a-layoff.md)
- **Look for Other Roles**
  - `ref/hr/run-a-layoff`, activity 13 -
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
