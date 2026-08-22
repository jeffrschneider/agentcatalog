# The records this abstract agent must leave

This is the contract. An agent implementing `quote-builder` leaves the
following behind, on every run.

Per quote: every line with the card version its price was read from,
what was netted off with the contract each deduction came from, the
discount asked for line by line with the evidence behind it, the margin
on the deal as asked and every line below the floor, each exception with
the person who may sign it and the reason it was asked for, and the
assembled quote at a version with the date it stops holding. When a term
is repriced smaller, the new price and its distance from the floor are
recorded beside the old one rather than replacing it.

An agent that leaves less than this does not implement `quote-builder`,
whatever else it does well.
