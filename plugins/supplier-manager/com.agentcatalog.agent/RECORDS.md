# The records this abstract agent must leave

This is the contract. An agent implementing `supplier-manager` leaves
the following behind, on every run.

The register holds one entry for each supplier, subscription, agreement,
membership and registration: what it is for, the agent or the person who
owns it, what it costs, the term, the renewal date, and the notice a
cancellation needs. An entry missing an owner or a renewal date is
recorded as missing them rather than left out of the register. For every
search, the requirements and the criteria at a version with the date
they were written, the candidates that were looked at and where each one
came from, the candidates dropped before scoring with the requirement
each one failed, and what the search itself cost to run. Every answer a
candidate gave, attributed to the candidate and dated. A dated notice
for each renewal, naming who was told, when they were told, and what the
owner decided. For every entry that ended, the date it ended, who
decided to end it, and what happened to the material or the data the
outside party was holding. For every registration, what was registered,
with which body, on what date, and when it has to be renewed.

An agent that leaves less than this does not implement
`supplier-manager`, whatever else it does well.
