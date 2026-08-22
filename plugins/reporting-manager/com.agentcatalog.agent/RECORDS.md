# The records this abstract agent must leave

This is the contract. An agent implementing `reporting-manager` leaves
the following behind, on every run.

The report at a version for each period, with every line attributed to
its source and set beside the commitment it is measured against. A dated
record of what it asked for, who answered, and who did not. A correction
goes out as a new version of the report, and the version it corrects
stays where it was.

An agent that leaves less than this does not implement
`reporting-manager`, whatever else it does well.
