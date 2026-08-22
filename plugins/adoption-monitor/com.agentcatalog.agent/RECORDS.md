# The records this abstract agent must leave

This is the contract. An agent implementing `adoption-monitor` leaves
the following behind, on every run.

Per process: the watched steps, and the unwatched ones with the reason
each was left out. For each watched step, the observable difference
between a followed run and a departed one. The change request field by
field, saying what each new field records about a person, and the policy
check with the line behind every refusal and the fields the privacy
reviewer struck out. The baseline, and the detection's score against the
known runs with every miss and every false alarm listed. Every signal
raised in the first weeks, checked by hand against the run it fired on.
The steps it still cannot see. Per period: the measure's gaps and
outages marked before a number is read, the ranked departures with the
count behind each rate, and what people said, attributed to a role, with
the refusals counted as refusals.

An agent that leaves less than this does not implement
`adoption-monitor`, whatever else it does well.
