# The records this abstract agent must leave

This is the contract. An agent implementing `background-check` leaves
the following behind, on every run.

Each run leaves the checks the screening policy set for the role in each
location with the reason for each, the point the rules let each one run,
the notice the candidate received and their signed consent to each
check, each order with the details sent and the date, and each check
chased to its result. The results sit in the restricted store with a log
of every opening, and the hiring record holds only the outcome. Where a
check found something, the run leaves the copy the candidate received
and the date, the time allowed to respond, the candidate's explanation
or the error sent back and the corrected result, the named person's
decision with the reason in terms of the job, and the written notice of
that decision with the rights the rules require. Each run closes with
the outcome handed to the offer, the date the results and references
were destroyed with a record that they were, and how long each check
took. Nothing in the record shows this agent deciding on a finding.

An agent that leaves less than this does not implement
`background-check`, whatever else it does well.
