# The records this abstract agent must leave

This is the contract. An agent implementing `content-manager` leaves the
following behind, on every run.

The request as it was accepted, with the date the piece promised and
what the piece is meant to accomplish. The CONVENED and DONE records of
everything it convenes. The publish record, naming who said go and which
version went live. The performance readout at the cadence the process
sets, and the decision it made after reading that readout: leave the
piece alone, update it, or retire it.

An agent that leaves less than this does not implement
`content-manager`, whatever else it does well.
