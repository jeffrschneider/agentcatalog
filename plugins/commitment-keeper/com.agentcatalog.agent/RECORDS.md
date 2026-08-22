# The records this abstract agent must leave

This is the contract. An agent implementing `commitment-keeper` leaves
the following behind, on every run.

Each commitment as an item carrying one owner, one date and a state,
traceable to the line of the signed plan it came from. At every review,
the roll-call of all of them with the late ones counted. Each closed
commitment with the reason it was given up on and the date. The
decisions from the review with the new owners and the new dates, and
every move of a date with the review that moved it, so a commitment that
has slipped twice can be seen to have slipped twice. The review dates
set for the year, and whose calendars they landed on.

An agent that leaves less than this does not implement
`commitment-keeper`, whatever else it does well.
