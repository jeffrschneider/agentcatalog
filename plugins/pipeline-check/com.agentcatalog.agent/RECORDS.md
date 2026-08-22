# The records this abstract agent must leave

This is the contract. An agent implementing `pipeline-check` leaves the
following behind, on every run.

Per run: the rules and stage definitions at the version they were read
at, the extract every check ran against, and the staleness numbers with
who agreed them. Per finding: the deal, the rule it failed, the amount
it moves, the person it was sent to and the date it was sent. Withdrawn
findings are kept as withdrawn with the reason, and a dispute is kept
whether or not the finding stood, because a rule many owners dispute is
the next amendment. Every mark carried into the roll-up names its rule
and its date. Somebody auditing a run can replay each finding against
the extract behind it.

An agent that leaves less than this does not implement `pipeline-check`,
whatever else it does well.
