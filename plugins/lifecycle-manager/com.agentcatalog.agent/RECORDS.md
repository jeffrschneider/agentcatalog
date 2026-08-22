# The records this abstract agent must leave

This is the contract. An agent implementing `lifecycle-manager` leaves
the following behind, on every run.

For each customer, the run at a version: the date they entered, the
condition that put them in, the goal the run is trying to reach, every
step they were given with the date and the reason it was chosen, and
every step that was skipped with the reason it was skipped. A dated line
each time the path changed, naming what changed and what the customer
did or failed to do that changed it. Every commitment made to the
customer, naming who made it, what was promised, when it is due, and the
date it was met. The handover record when a person takes over, saying
what that person is being asked to do and everything the customer has
already been sent. The closing record, saying whether the goal was
reached, what the customer did, and the date the run ended.

An agent that leaves less than this does not implement
`lifecycle-manager`, whatever else it does well.
