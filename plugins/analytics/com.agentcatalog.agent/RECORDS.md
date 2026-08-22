# The records this abstract agent must leave

This is the contract. An agent implementing `analytics` leaves the
following behind, on every run.

Every report with every line attributed to its source, delivered on the
cadence the process sets. A missing source appears in the report as
missing.

An agent that leaves less than this does not implement `analytics`,
whatever else it does well.
