# The records this abstract agent must leave

This is the contract. An agent implementing `application-screener`
leaves the following behind, on every run.

Each application read leaves its note at a version, with the hiring plan
version it was read against, each point citing its must-have, what the
application shows for it and what it leaves unclear. Each flag leaves
the application it concerns and the reason it could not be read fairly.
Each note the recruiting-coordinator agent struck or sent back is kept
with the reason and the note written in its place. Nothing in the record
shows this agent ranking, turning down or choosing an applicant, and
nothing in a note refers to a withheld detail or a protected
characteristic.

An agent that leaves less than this does not implement
`application-screener`, whatever else it does well.
