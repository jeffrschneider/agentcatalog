# The records this abstract agent must leave

This is the contract. An agent implementing
`employee-question-responder` leaves the following behind, on every run.

Each question leaves what was asked, the channel it came through, the
time it arrived and the answer time set for it, the match of the asker
to one employee record, and the reading of whether it is personal or
sensitive. An answered question leaves the facts read to choose the
answer, the approved answer with its source and its version, the check
against the policy text, the time it was sent, and whether the employee
said it settled the question. A passed question leaves only its subject,
the reason it was passed and the named person who took it. A records
request leaves the request as recognized, the acknowledgment with its
deadline in the approved text, and each question about the answer
answered from the approved text or passed to the privacy lead. Nothing
in the record shows this agent approving, refusing or promising leave, a
pay change, an accommodation or any other decision about a person.

An agent that leaves less than this does not implement
`employee-question-responder`, whatever else it does well.
