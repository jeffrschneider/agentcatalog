# The records this abstract agent must leave

This is the contract. An agent implementing `relationship-mapper` leaves
the following behind, on every run.

Per person: the decision they sit under, whether they decide, influence,
block or use, the source they were found in and that source's
publication date, the reporting line behind any claim of authority, the
strength score with the contact history it was computed from, the path
in and who at our end holds it, and the stance with what was said or
done behind it. Per map: every decision with no decider found or nobody
we know marked as a gap rather than left blank, what the privacy check
removed and the rule behind each removal, and the issued version naming
who corrected what and when they signed. A claim that somebody knows a
buyer well is recorded as a claim, with the person who made it.

An agent that leaves less than this does not implement
`relationship-mapper`, whatever else it does well.
