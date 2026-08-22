# The records this abstract agent must leave

This is the contract. An agent implementing `lead-scorer` leaves the
following behind, on every run.

Per lead: the merged record with each filled field naming its source,
the score with the model version and the inputs it was computed from,
and the assignment with the reason. Any auditor can replay any decision
from what it left behind.

An agent that leaves less than this does not implement `lead-scorer`,
whatever else it does well.
