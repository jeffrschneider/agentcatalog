# The records this abstract agent must leave

This is the contract. An agent implementing `community-manager` leaves
the following behind, on every run.

Every reply logged, every escalation with the reason it was flagged, and
a recurring-questions summary at the cadence the process sets.

An agent that leaves less than this does not implement
`community-manager`, whatever else it does well.
