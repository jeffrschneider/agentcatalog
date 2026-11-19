# The records this abstract agent must leave

This is the contract. An agent implementing `workforce-planner` leaves
the following behind, on every run.

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

An agent that leaves less than this does not implement
`workforce-planner`, whatever else it does well.
