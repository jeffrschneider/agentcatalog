# The records this abstract agent must leave

This is the contract. An agent implementing `supplier-check` leaves the
following behind, on every run.

It leaves a scoring sheet for each candidate at a version, naming the
requirements list and the version it scored against, with one row per
requirement carrying the verdict and the evidence behind it. The
evidence names the demonstration step, the document, or the reference
call it came from, so a person can check a verdict without asking the
agent what it meant. A requirement it could not test is recorded as not
tested, with the reason it could not be tested. When a candidate revises
its material, the rescore says what changed, what was run again, and
what was carried over from the earlier score. It records the date each
candidate's material arrived and the date it was scored.

An agent that leaves less than this does not implement `supplier-check`,
whatever else it does well.
