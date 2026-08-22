# The records this abstract agent must leave

This is the contract. An agent implementing `press-relations` leaves the
following behind, on every run.

A line for every contact, giving the date, the person, the material it
sent at its version, what that person asked, and what it gave them. The
contact record kept current, so anybody can see who covers this subject
and what they have already written. Every briefing with who attended,
what was shown, what was said under what terms, and what was promised
afterwards. The list of follow-ups it owes, each with the date it was
promised and the date it was delivered.

An agent that leaves less than this does not implement
`press-relations`, whatever else it does well.
