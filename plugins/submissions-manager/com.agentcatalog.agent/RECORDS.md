# The records this abstract agent must leave

This is the contract. An agent implementing `submissions-manager` leaves
the following behind, on every run.

The submissions record holds one entry for each body, with the
eligibility rules as they were read, the date they were read, the
deadline, and the format the body requires. Every filed entry is kept at
the version that was filed, with the date it went in and the sign-off it
went out under. Every question the judges or the analysts asked is
recorded with the answer given and the date it was given. The decision
is recorded when it arrives, together with what the body said about the
entry and whether the entry won.

An agent that leaves less than this does not implement
`submissions-manager`, whatever else it does well.
