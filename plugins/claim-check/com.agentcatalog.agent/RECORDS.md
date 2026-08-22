# The records this abstract agent must leave

This is the contract. An agent implementing `claim-check` leaves the
following behind, on every run.

Per claim: the approval it was checked against, at its version, and the
evidence list agreed at that approval. The completeness check, naming
every document the approval asked for and whether it arrived. The match
between the activity claimed and the activity approved, on date, place
and scope. Each evidence item marked present, missing or insufficient.
Each cost line scored against the eligible activity list at its version,
with the rule it passes or fails. The invoice check, naming amounts,
dates, tax treatment and who was actually paid. The duplicate check,
naming where else a cost appeared if it did. The score, with the amount
payable, the amount cut, and a reason on every cut. For any line the
rules could not reach, the person who decided it and what they decided.
A run can be replayed line by line from what it left behind.

An agent that leaves less than this does not implement `claim-check`,
whatever else it does well.
