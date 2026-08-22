# The records this abstract agent must leave

This is the contract. An agent implementing `buy-check` leaves the
following behind, on every run.

A verdict per item, each citing the plan line or the rule, its version,
and the campaign configuration it was read against. A pre-launch score
and a post-delivery score, each dated and each naming what it read.
Anything it could not test is recorded as untested rather than left out.
A rescore after a fix names what changed and what it ran again. Where
what ran differs from what was ordered, the difference is recorded
against the plan line it belongs to, with the figures on both sides.

An agent that leaves less than this does not implement `buy-check`,
whatever else it does well.
