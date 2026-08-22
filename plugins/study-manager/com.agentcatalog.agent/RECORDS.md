# The records this abstract agent must leave

This is the contract. An agent implementing `study-manager` leaves the
following behind, on every run.

The study written down as a question before any data is gathered: what
it has to settle, the method chosen and why that method, who or what is
sampled, how many responses it needs, and the date the findings are due.
Every question and every piece of material at a version, in the order it
is put to people, with each response marked with the version it
answered. Every response as it was given, with its date, and every
response that was removed from the count, with the rule that removed it.
Each finding with the responses recorded under it, so the finding and
its evidence are read together. A comparison against the earlier studies
in the series, naming every place this study differs from the last one
and what that difference does to the reading. The count of responses
against the count the study planned for, said on the day the study
closes. The CONVENED and DONE records of everything it convenes.

An agent that leaves less than this does not implement `study-manager`,
whatever else it does well.
