# The records this abstract agent must leave

This is the contract. An agent implementing `partner-qualifier` leaves
the following behind, on every run.

The claim register at a version: every claim that decides the answer,
marked proven, unproven or false, naming what settled it, where that
came from and the date it was read. The reference notes with the
question set they were taken against, and which references we found
rather than were offered. The real-work record, naming the data it ran
on and who cleared that data. The residual risk with the assumption
behind each number. Anyone auditing the run can recompute the
recommendation from what is on the record, or say which claim they would
mark differently.

An agent that leaves less than this does not implement
`partner-qualifier`, whatever else it does well.
