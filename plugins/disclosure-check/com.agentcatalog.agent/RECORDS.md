# The records this abstract agent must leave

This is the contract. An agent implementing `disclosure-check` leaves
the following behind, on every run.

A verdict per item, each citing the rule, its version, the market it
applies in, and the version of the material it was read against. The
market and channel list the piece was scored against, recorded with the
score, so a later run into a new market is scored again. Where a rule
requires particular wording, the wording it requires, recorded beside
the item. A market the organization holds no rules for is recorded as
unscored. A rescore after a fix names what changed and what it ran
again.

An agent that leaves less than this does not implement
`disclosure-check`, whatever else it does well.
