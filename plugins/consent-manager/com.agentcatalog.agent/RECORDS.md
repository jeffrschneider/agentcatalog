# The records this abstract agent must leave

This is the contract. An agent implementing `consent-manager` leaves the
following behind, on every run.

For every list it clears, the count it removed and the rule each removal
was made under. For every withdrawal, a dated line naming each system
that keeps a copy of the audience, when the withdrawal was written into
it, and when the write was confirmed. A verdict per item for a scored
change, each citing the rule and its version. For every send it stopped,
the rule the send would have broken and the contacts it would have
reached.

An agent that leaves less than this does not implement
`consent-manager`, whatever else it does well.
