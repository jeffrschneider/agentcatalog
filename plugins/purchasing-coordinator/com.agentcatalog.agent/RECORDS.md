# The records this abstract agent must leave

This is the contract. An agent implementing `purchasing-coordinator`
leaves the following behind, on every run.

Each request leaves what was asked for with the requester, the amount,
the budget line and the dates, any field asked for again and when it
came, the supplier's record and, above the threshold, the choice behind
it, and any request held for a choice or a setup with the date it was
expected. Beside it sit the room the budget-keeper agent found, the
approvals the delegation-keeper agent counted and the commitment
recorded. Each order leaves its versions with their terms, the date it
was sent and the contact it went to, the supplier's acceptance or the
change it asked for, each receipt with who confirmed it, the quantity
and the date, anything damaged, short or late with the reason, and the
close with the amount released from the line. Work started or goods
delivered before an order was approved are recorded as an exception.
Each period leaves the list of what was received and not yet invoiced
and the capital purchases passed to the register. Nothing in the record
shows this agent approving a purchase, committing money or moving money
between budget lines.

An agent that leaves less than this does not implement
`purchasing-coordinator`, whatever else it does well.
