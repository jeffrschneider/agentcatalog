# The records this abstract agent must leave

This is the contract. An agent implementing `moderator` leaves the
following behind, on every run.

Every action, with the post as it stood when it was read, the rule and
its version, the action taken, how long that action lasts, the time it
was taken, and the notice that went to the member. A post it read and
left alone is recorded where the process asks for that. An appeal is
recorded with the person's decision, and a reversal lands as a new
record while the original action stays where it is.

An agent that leaves less than this does not implement `moderator`,
whatever else it does well.
