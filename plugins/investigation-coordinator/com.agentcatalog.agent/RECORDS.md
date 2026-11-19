# The records this abstract agent must leave

This is the contract. An agent implementing `investigation-coordinator`
leaves the following behind, on every run.

Each investigation leaves each allegation as a question with the policy
clause it would breach and the investigator's approval, the plan of
witnesses, records and dates as the investigator approved it, and each
record listed for the hold with the date the HR system administrator
held it. It leaves each interview booked with its time, its place and
any companion, and an evidence log of every document, message, record
and set of interview notes with its source, its date and who gave it. It
leaves the timeline of events in order, each with its evidence and each
place where the accounts differ, and for each allegation the evidence
that supports it and the evidence against it, each with its source, with
the questions still open. A new allegation is recorded as a new question
with the date the person it is about was told of it in writing. The log
is closed as it stands when the findings are signed or the run is
abandoned. Nothing in the record shows this agent drawing a finding,
because the findings are the investigator's.

An agent that leaves less than this does not implement
`investigation-coordinator`, whatever else it does well.
