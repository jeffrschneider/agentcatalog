# The records this abstract agent must leave

This is the contract. An agent implementing `offer-builder` leaves the
following behind, on every run.

Each offer leaves the decision with the reserves in order, the outcome
of the checks read as clear, decided or conditional with nothing about
what a check found, the agreed terms with the compensation-analyst
agent's check beside them, and each version of the letter with its
expiry date, any condition it carries and every change from the last
version marked. Beside each version sit the approvers' signatures in the
set order and their dates, and the date the recruiter made the offer and
the letter went out. Each ask is read against the limits and marked
inside or past them, with the approvers' written answer to any ask past
them. The run closes with the signed acceptance, the agreed start date
and the final terms, a conditional offer confirmed once the checks
cleared, and the hire handed to onboarding. Nothing in the record shows
this agent approving, changing or withdrawing an offer on its own.

An agent that leaves less than this does not implement `offer-builder`,
whatever else it does well.
