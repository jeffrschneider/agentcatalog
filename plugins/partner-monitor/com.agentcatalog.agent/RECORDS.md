# The records this abstract agent must leave

This is the contract. An agent implementing `partner-monitor` leaves the
following behind, on every run.

For every reading: the period it covers, the measure set at its version,
the source of each number and the date it was pulled, so somebody else
can recompute it. What the partner owed and what the company owed, read
in the same round and reported together. Every difference between our
count and the partner's, marked settled or open, with what is missing.
Everything it could not read, marked unread and naming the data that was
not there. A dated line for every certificate that lapsed and every
certified person who left. At an ending, the list of customers the
partner holds, the work still in flight, and the confirmation that names
anything that could not be closed.

An agent that leaves less than this does not implement
`partner-monitor`, whatever else it does well.
