# The records this abstract agent must leave

This is the contract. An agent implementing `expense-check` leaves the
following behind, on every run.

Each claim and each card transaction leaves every line with its receipt,
its business reason, its amount and currency, the rate it was converted
at, and the policy rule and version it was read against, returned as
inside the policy, outside it with the rule it breaks, or missing its
evidence. Beside each line sit any earlier claim, card transaction or
booking it repeats, any part marked as treated as pay with the rule
behind it, each question asked of the employee with the answer, and each
reminder sent to the manager. Each claim closes with which lines were
outside the policy and why, which rules caught most and how long the
claim took. Nothing in the record shows this agent approving, refusing
or paying a line.

An agent that leaves less than this does not implement `expense-check`,
whatever else it does well.
