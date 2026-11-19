# The records this abstract agent must leave

This is the contract. An agent implementing `filing-coordinator` leaves
the following behind, on every run.

Each filing leaves the authority, the location, the period, the form,
the deadline and the named signer, counsel's answer on whether the form
or the rule changed, the fields gathered at their date and nothing more,
the filing at a version with each figure traced to its data, each change
from the last filing explained, the review and the signature with who
gave them, the date it was filed, and the receipt, the filed copy and
the data kept for `<your jurisdiction's retention period>`. It also
leaves each follow-up and correction, and the next date on the calendar
with its lead time. The payroll year end leaves every return and
deadline for each place with the timetable counted back from it, each
annual return prepared from the reconciled figures, the check of the
statements against the returns person by person and in total, each
return filed with its receipt, and any corrected return with its own
receipt beside the first. An audit leaves the authority, the scope, the
period and every date, each request numbered with its due date and its
owner, each response as signed and sent with what went, when, to whom
and at which version, every record shown and question asked during an
inspection, each finding with what it rests on, its owner and its date,
and the closing letter with the hold lifted. Nothing in the record shows
this agent signing a filing or deciding the company's position on a
finding.

An agent that leaves less than this does not implement
`filing-coordinator`, whatever else it does well.
