# The records this abstract agent must leave

This is the contract. An agent implementing `roll-up-builder` leaves the
following behind, on every run.

The cut-off with its time zone, and the cut-off the last cycle used. The
extract with its row count and its total. Every deal in one currency,
with its original amount, its currency and the rate beside it. Every
deal's category as the definition produces it, next to the category the
record claimed. Every cut with the count of deals behind each total, and
the reconciliation to the extract with any difference shown deal by deal
rather than as a rounding line. The comparison to the last cycles, with
every definition, rate or cut-off change marked at the cycle it
happened. The questions this roll-up could not answer, each with the
reason. The frozen version with its name and its timestamp, and the
figures the second check rebuilt from the extract.

An agent that leaves less than this does not implement
`roll-up-builder`, whatever else it does well.
