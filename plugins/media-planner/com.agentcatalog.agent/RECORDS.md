# The records this abstract agent must leave

This is the contract. An agent implementing `media-planner` leaves the
following behind, on every run.

The plan at a numbered version, one row per line: the channel, the dates
it runs, the weight it runs at, the audience it is bought against, and
the money committed to it. Every earlier version stays readable at its
own number, so a buy can be checked against the plan it was placed
under. A change record for each version, saying which lines moved, by
how much, why, and who approved it. A dated position saying what is
committed, what has been placed, and what is still free, with the
figures those came from. Every request for money the plan could not
cover, with the amount asked for and the answer it got.

An agent that leaves less than this does not implement `media-planner`,
whatever else it does well.
