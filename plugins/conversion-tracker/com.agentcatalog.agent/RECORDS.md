# The records this abstract agent must leave

This is the contract. An agent implementing `conversion-tracker` leaves
the following behind, on every run.

A measurement plan at a version, naming every conversion, what counts as
one, and where it fires. For each conversion, a dated test record
showing a real submission arriving in the CRM. The tracking parameters
it handed to each paid channel, recorded against the page they belong
to. Anything it could not verify is recorded as unverified rather than
left out.

An agent that leaves less than this does not implement
`conversion-tracker`, whatever else it does well.
