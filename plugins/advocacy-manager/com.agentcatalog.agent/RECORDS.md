# The records this abstract agent must leave

This is the contract. An agent implementing `advocacy-manager` leaves
the following behind, on every run.

For each ask, it records the customer, what was asked for, who asked,
the date, and the answer that came back. An agreement records its terms
in the customer's own words: what may be used, in which channels, under
which name and title, and until when, together with the approval the use
rests on. A refusal records the reason the customer gave and the date
they may be asked again. Beside those, it keeps a standing list of which
customers are available for which kind of ask, current as of a date, so
that no run plans around a customer who never agreed to it.

An agent that leaves less than this does not implement
`advocacy-manager`, whatever else it does well.
