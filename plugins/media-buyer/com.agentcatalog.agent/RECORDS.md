# The records this abstract agent must leave

This is the contract. An agent implementing `media-buyer` leaves the
following behind, on every run.

Every campaign configuration at a version, every budget move with the
number, the direction, and the reason, and the stop record when the buy
comes off.

An agent that leaves less than this does not implement `media-buyer`,
whatever else it does well.
