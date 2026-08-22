# The records this abstract agent must leave

This is the contract. An agent implementing `event-program` leaves the
following behind, on every run.

The call for sessions at a version, saying what a proposal has to
contain and the date it closes. Every proposal that arrived, with the
verdict it was given and the criterion behind that verdict, including
the proposals that were turned down. The agenda at a version each time
the running order changes, naming what moved and why. For each speaker,
the brief they were given, everything they owe with its deadline, what
has arrived at which version, and every change they were told about with
the date they were told. The rehearsal record, saying which speakers
rehearsed, which did not, and what was still unresolved when the
rehearsal ended.

An agent that leaves less than this does not implement `event-program`,
whatever else it does well.
