# The records this abstract agent must leave

This is the contract. An agent implementing `integration-keeper` leaves
the following behind, on every run.

Per link: the systems either side with the person who owns each, the
agreed flows at a version naming every field, its direction, its cadence
and what starts the move, and the system of record per field with who
decided where the owners could not agree. The known set moved through
the link with the counts on both sides, field by field, and every
difference. The failure test, saying what the link retried, duplicated,
dropped and queued when it was broken on purpose. The cleared review
with the date it was signed and every finding accepted rather than
fixed. The date and hour it went live, and the way back as it was
written down before the switch. The first runs and the reconciled
counts, dated, with the reason behind every difference where one is
known. The record of what flows where at its version, naming the fields
it does not yet cover. When a link stops, what it was carrying and where
that now comes from.

An agent that leaves less than this does not implement
`integration-keeper`, whatever else it does well.
