# The records this abstract agent must leave

This is the contract. An agent implementing `margin-keeper` leaves the
following behind, on every run.

The priced tier table at a version, naming the rules version it was
priced against, the volume each tier assumes, and the margin, discount,
fund and support hours each one carries. The margin test per tier,
naming the floor it was set against and the shortfall where there is
one, with the name of whoever accepted a shortfall in writing. Per
partner, the discount in force and the date it started. Per system
changed, what it was set to and the date it took effect. For a
relationship ending, the settlement line by line: what was earned, what
was paid, what is recovered, and what is still open. For a performance
round, what the company owed each partner set against what was actually
delivered, with each difference settled or marked open.

An agent that leaves less than this does not implement `margin-keeper`,
whatever else it does well.
