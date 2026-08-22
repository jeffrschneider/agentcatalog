# The records this abstract agent must leave

This is the contract. An agent implementing `qualifier` leaves the
following behind, on every run.

The questions as written before they were asked, naming the version of
the question set they came from. Per question: the answer in the words
it came back in, or the mark that says unanswered, unclear, contradicted
or declined. Nothing is filled in with an assumption. The fit check line
by line against the profile version. The gaps, listed. The decision, who
made it, the date, the reason, and the evidence under it. For a return:
the reason taken from the reason list, the date to look again, the
signals that would end the wait early, the note that went back with the
lead, and what the wait eventually produced.

An agent that leaves less than this does not implement `qualifier`,
whatever else it does well.
