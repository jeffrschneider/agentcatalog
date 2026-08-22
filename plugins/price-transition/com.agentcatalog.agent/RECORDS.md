# The records this abstract agent must leave

This is the contract. An agent implementing `price-transition` leaves
the following behind, on every run.

The register at a version, giving for each customer what they pay now,
what the new prices make them pay, the amount and the share of the
change, the grandfathering rule that caught them and the date that rule
runs out, the notice they are owed, and the earliest date their change
may take effect. A dated line for every notice served, naming the
customer, the version of the wording that went, the date it went, the
route it went by, and the date its waiting time runs out. A dated line
for every price change released, naming the customer, the date the new
price takes effect, and the notice record that cleared it. A customer it
could not sort is recorded as unsorted, with what is missing, rather
than being left out of the register. A change it is holding back is
recorded as held, with the reason and the number of days it has been
held.

An agent that leaves less than this does not implement
`price-transition`, whatever else it does well.
