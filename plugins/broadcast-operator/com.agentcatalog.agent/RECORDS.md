# The records this abstract agent must leave

This is the contract. An agent implementing `broadcast-operator` leaves
the following behind, on every run.

The session as it was set up, at a version, saying the date, the time,
who may join and how, what material was loaded, and which polls were
prepared. The rehearsal record, saying which presenters connected, which
were heard, which shared successfully, what failed, and what was still
unresolved when the rehearsal ended. A dated record of the live session,
saying when it started, when it ended, who was on air at each point,
when each poll opened and closed, and anything that went wrong with the
time it happened. The recording at a version. The attendance record,
naming who registered, who joined, when each person joined and left, and
how long they stayed. The poll answers as the platform recorded them.
Every question that was asked, with the time it came in, whether it was
answered on air, and which questions were still unanswered when the
session ended.

An agent that leaves less than this does not implement
`broadcast-operator`, whatever else it does well.
