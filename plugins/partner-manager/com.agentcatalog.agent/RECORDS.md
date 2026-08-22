# The records this abstract agent must leave

This is the contract. An agent implementing `partner-manager` leaves the
following behind, on every run.

The partner record at a version, naming the agreement it rests on, the
tier the partner holds, the date that tier was set and who set it. For
everything the partner was given, the version it was at and the date it
went to them. For every person the partner put through training, what
they were trained on and the date they finished. A dated line for each
obligation as it comes due, saying whether it was met and by whom. What
the partner delivered back, counted against what the agreement asked
for, at the cadence the process sets. The CONVENED and DONE records of
everything it convenes, and the approval record behind every release and
every tier change.

An agent that leaves less than this does not implement
`partner-manager`, whatever else it does well.
