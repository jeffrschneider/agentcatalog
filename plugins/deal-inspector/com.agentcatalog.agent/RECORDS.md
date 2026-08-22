# The records this abstract agent must leave

This is the contract. An agent implementing `deal-inspector` leaves the
following behind, on every run.

Per inspection: the deal record with every change to stage, amount and
date carrying its author. The buying group, each named person marked met
or unmet. What the customer said, dated and quoted, and every place the
record holds nothing. The budget, the approver, and whether the money is
committed elsewhere. Who else is in it and what would have to be true to
win. Every remaining step with its owner and the time it takes, and
whether they fit before the close date or by how much they miss. Every
claim marked evidenced, asserted or absent, with the record and the date
behind each evidenced one. The one or two things that decide the deal.
The owner's answers as given, the actions with owners and dates, and the
category with who set it and their reason. Per loss: the signal, who
confirmed the decision, the loss date, the buyer's own words kept beside
one reason code, the winner or the decision to do nothing, any
contradiction between the stated reason and the record, and the
follow-up date with what would have to change.

An agent that leaves less than this does not implement `deal-inspector`,
whatever else it does well.
