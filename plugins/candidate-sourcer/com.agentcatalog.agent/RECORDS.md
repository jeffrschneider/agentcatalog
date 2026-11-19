# The records this abstract agent must leave

This is the contract. An agent implementing `candidate-sourcer` leaves
the following behind, on every run.

Each search leaves the hiring plan at the version it searched for, the
request for referrals and the teams it went to, each referral with the
employee who made it, how they know the person and the person's
agreement to be contacted, and each person found recorded once with the
first source that found them and the date. Each person carries the
reading against the must-haves with the evidence found for each and what
is still unclear, and the check of who may be approached with the reason
anyone was left out. Each approach is kept as drafted with where the
person's details came from, beside the recruiter's choice and the date
it was sent, with at most one follow-up. The search closes with each
person who said yes added as a candidate with their source, who said no
or did not reply and when each may be approached again, a record that
the details of the rest were removed and when, and how many each source
found and sent forward. Nothing in the record shows this agent sending
an approach or giving a referral weight in the screen.

An agent that leaves less than this does not implement
`candidate-sourcer`, whatever else it does well.
