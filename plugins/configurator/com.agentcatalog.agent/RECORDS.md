# The records this abstract agent must leave

This is the contract. An agent implementing `configurator` leaves the
following behind, on every run.

Per run: the entitlement read, dated, with the contract each line came
from and the end date of each one. The configuration at a version, with
the reason behind every option that is not the default. The check result
naming each rule tested, each failure, and the rule behind any failure
that was accepted anyway. The quote check scored against the
configuration version and the rate card version it claims. The closing
record of what was configured, what it priced at, and what each approval
took. Somebody replaying the run can see why every line is in the
configuration and why it passed.

An agent that leaves less than this does not implement `configurator`,
whatever else it does well.
