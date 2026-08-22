# The records this abstract agent must leave

This is the contract. An agent implementing `standards-keeper` leaves
the following behind, on every run.

Every standard at a numbered version, with the date it took effect and
the date it stopped being current. A change record for each version,
saying what changed, what it replaced, who approved it, and when. Every
earlier version left readable at its own number, so work can be judged
against the standard it was made under. Every interpretation it issued,
attached to the rule and the version it interprets, carrying the
question that prompted it and the agent that asked. A dated record of
who was told about each change.

An agent that leaves less than this does not implement
`standards-keeper`, whatever else it does well.
