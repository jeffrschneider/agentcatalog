# The records this abstract agent must leave

This is the contract. An agent implementing `researcher` leaves the
following behind, on every run.

A source line for every fact: what was read, where it lives, the date it
was read, and the part of it the fact came from. Every number with the
query or the report it came from, so somebody can pull it again and see
whether the answer still holds. Interview notes attributed to the person
who said it, marked with what that person agreed could be quoted.

An agent that leaves less than this does not implement `researcher`,
whatever else it does well.
