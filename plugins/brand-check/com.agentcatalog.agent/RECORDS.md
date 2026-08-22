# The records this abstract agent must leave

This is the contract. An agent implementing `brand-check` leaves the
following behind, on every run.

A score per item, each citing the standard, its version, and the rule
applied. What passed, what failed, and why, in a form the human signers
read in minutes.

An agent that leaves less than this does not implement `brand-check`,
whatever else it does well.
