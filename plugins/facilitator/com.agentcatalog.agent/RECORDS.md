# The records this abstract agent must leave

This is the contract. An agent implementing `facilitator` leaves the
following behind, on every run.

Its phase calls, plan statements, turn namings and departure notes, each
a signed message in the conversation's own record. It keeps no second
copy and produces no minutes document, because the record already holds
everything it did, signed, ordered and attributable - a separate minutes
document would be a weaker copy of the books.

An agent that leaves less than this does not implement `facilitator`,
whatever else it does well.
