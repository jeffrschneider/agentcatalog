# The records this abstract agent must leave

This is the contract. An agent implementing `capacity-manager` leaves
the following behind, on every run.

It leaves the book of work at a version for each period, with every
request carrying the date it arrived and its current state, and every
committed run carrying the agents it needs and the dates it holds. Every
commitment it makes is recorded with the date it was made and what it
displaced, and every commitment that changes is recorded the same way.
It records what each activity actually took against the run it came
from, so the department's estimates come from its own history. The room
left in the period is restated whenever a commitment lands or moves. A
request the department could not take is recorded with the reason and
the date, and it stays in the book.

An agent that leaves less than this does not implement
`capacity-manager`, whatever else it does well.
