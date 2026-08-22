# The records this abstract agent must leave

This is the contract. An agent implementing `web-producer` leaves the
following behind, on every run.

The page at a version, with the preview link that shows it. The publish
record naming the version, the time, and the person who said go. Every
redirect it set, with the address it came from and the address it now
points at. The rollback record when a page comes down, saying what is in
its place.

An agent that leaves less than this does not implement `web-producer`,
whatever else it does well.
