# The records this abstract agent must leave

This is the contract. An agent implementing `campaign-manager` leaves
the following behind, on every run.

The run's plan, the CONVENED and DONE records of everything it convenes,
the launch record naming who said go, and the final report against the
brief.

An agent that leaves less than this does not implement
`campaign-manager`, whatever else it does well.
