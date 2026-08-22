# The records this abstract agent must leave

This is the contract. An agent implementing `creator-relations` leaves
the following behind, on every run.

For each creator, the record holds the audience figures with the date
they were read and the source they came from, what the authenticity
check found, and what the history check found in the creator's past
publishing. For each deal, it keeps what was agreed at the version it
was agreed: every deliverable, the date each one is due, the channels
the work may run on, how long the organization may use it, what the
disclosure has to say, and the fee. Every approach lands with its date,
what was offered, and the answer that came back, including the creators
who declined and the reason they gave. When a creator publishes, the
agent records what went out, where it went out, and on what date. When a
check finds a problem, the agent records the finding, what it asked the
creator to do, the date it asked, and what the creator did.

An agent that leaves less than this does not implement
`creator-relations`, whatever else it does well.
