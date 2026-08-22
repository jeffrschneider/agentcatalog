# The records this abstract agent must leave

This is the contract. An agent implementing `deduper` leaves the
following behind, on every run.

Per set: the records proposed as one thing, what proposed them and when,
the rule that matched with the fields it matched on and the strength it
matched at, and the score with the model version and the inputs it was
computed from. The person's answer with their name and the date, and
which record they called the real one. The surviving id and the reason
it was chosen over the other. Everything now pointing at the survivor,
and anything that could not be repointed. Both owners told, with the
date they were told. The merge as written, and the closed record
pointing at the survivor. Every value that did not survive, stored
against the survivor, dated, naming the record it came from, so a
reversal knows what it is putting back. A pair found not to be one thing
is marked as compared, with the rule that was wrong, so the same rule
stops proposing them.

An agent that leaves less than this does not implement `deduper`,
whatever else it does well.
