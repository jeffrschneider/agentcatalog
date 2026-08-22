# The records this abstract agent must leave

This is the contract. An agent implementing `terms-check` leaves the
following behind, on every run.

Per term: the clause of the standard it was scored against, the version
that clause was read at, whether it departs, in which direction, and how
far. Every term the standard has no clause for is recorded as unscorable
with the reason, never as passed. When it scores a draft approval table,
each band carries a pass or the rule behind its failure. Every score
names the item in the words it was given, so somebody auditing a run can
read the same clause at the same version and get the same answer without
asking this agent what it meant.

An agent that leaves less than this does not implement `terms-check`,
whatever else it does well.
