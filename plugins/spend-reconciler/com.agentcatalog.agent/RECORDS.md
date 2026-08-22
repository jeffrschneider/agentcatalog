# The records this abstract agent must leave

This is the contract. An agent implementing `spend-reconciler` leaves
the following behind, on every run.

The reconciliation for the period at a version, one row per line: what
was ordered, what ran, what was billed, the difference, and the amount
at stake. Against every unmatched line, the question that went to the
issuer, the date it went, the answer that came back, and what that
answer settled. A line still open on the day the period closes is
recorded as open, with its age and its amount. A credit is recorded
against the line it settles, so the next period is checked against a
figure that already accounts for it.

An agent that leaves less than this does not implement
`spend-reconciler`, whatever else it does well.
