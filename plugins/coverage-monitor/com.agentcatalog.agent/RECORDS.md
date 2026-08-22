# The records this abstract agent must leave

This is the contract. An agent implementing `coverage-monitor` leaves
the following behind, on every run.

One entry per mention, giving the outlet, the date it appeared, the
author, the headline, the address it lives at, and what the piece said
about the organization, quoted where the exact wording matters. Each
entry says whether the mention can be traced back to something the
organization sent out. A summary at the cadence the process sets,
covering what ran, where it ran, and how the tone moved since the last
one. A source it could not reach appears in the summary as unreached.

An agent that leaves less than this does not implement
`coverage-monitor`, whatever else it does well.
