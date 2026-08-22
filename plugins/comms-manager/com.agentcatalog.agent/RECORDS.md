# The records this abstract agent must leave

This is the contract. An agent implementing `comms-manager` leaves the
following behind, on every run.

The timeline at a version, saying what was known at each point, who
established it, and who was told. Each audience's wording at the version
that actually went out, with the versions it replaced left where they
are. The CONVENED and DONE records of everything it convenes. The go
record, naming the person who said go and the time they said it. The
report afterwards, setting what happened against what the announcement
or the response was meant to do.

An agent that leaves less than this does not implement `comms-manager`,
whatever else it does well.
