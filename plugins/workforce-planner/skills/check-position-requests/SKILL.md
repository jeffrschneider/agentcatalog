---
name: check-position-requests
description: Takes in a manager's request for a new or replacement position, checks it is complete and that the plan holds it, supports the department head's trade for an unplanned position, records the signed position on the plan, and hands it to the recruiter. Use it when running `ref/hr/open-a-position`.
license: CC-BY-4.0
metadata:
  agent: workforce-planner
  agent-version: "1"
---

# Check position requests

## What it does

Takes in a manager's request for a new or replacement position, checks
it is complete and that the plan holds it, supports the department
head's trade for an unplanned position, records the signed position on
the plan, and hands it to the recruiter.

## Where it happens

The agent does this in eight activities across one reference process.
Each one names the activity as that process words it.

- **Check the Request Is Complete**
  - `ref/hr/open-a-position`, activity 2 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Check the Request against the Plan**
  - `ref/hr/open-a-position`, activity 3 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Close the Request**
  - `ref/hr/open-a-position`, activity 14 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Hand the Position to Hiring**
  - `ref/hr/open-a-position`, activity 13 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Propose a Trade for an Unplanned Position**
  - `ref/hr/open-a-position`, activity 9 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Record the Position on the Plan**
  - `ref/hr/open-a-position`, activity 11 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Take in the Request**
  - `ref/hr/open-a-position`, activity 1 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)
- **Tell the Hiring Manager**
  - `ref/hr/open-a-position`, activity 12 -
    [Open a Position](../../../../processes/human-resources/open-a-position.md)

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
