# The records this abstract agent must leave

This is the contract. An agent implementing `compensation-analyst`
leaves the following behind, on every run.

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

An agent that leaves less than this does not implement
`compensation-analyst`, whatever else it does well.
