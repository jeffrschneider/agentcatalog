# The records this abstract agent must leave

This is the contract. An agent implementing `accessibility-check` leaves
the following behind, on every run.

A score per item, each citing the standard, its version and the rule
applied, against the page or asset version it scored. It reports what
passed, what failed, and what it could not test, in a form the signers
read in minutes. A rescore after a fix names what changed and what it
ran again.

An agent that leaves less than this does not implement
`accessibility-check`, whatever else it does well.
