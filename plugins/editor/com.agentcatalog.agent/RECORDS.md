# The records this abstract agent must leave

This is the contract. An agent implementing `editor` leaves the
following behind, on every run.

Every edit at a version, saying what has to change and why, item by
item, in terms the writer can work through without coming back to ask
what was meant. A line for anything it flagged for another pass, naming
the agent it went to. When it holds the version, the merge, the decline
or the revision request it gave in every round, each with its reason.

An agent that leaves less than this does not implement `editor`,
whatever else it does well.
