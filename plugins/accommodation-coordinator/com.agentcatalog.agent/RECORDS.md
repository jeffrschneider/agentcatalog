# The records this abstract agent must leave

This is the contract. An agent implementing `accommodation-coordinator`
leaves the following behind, on every run.

Each request leaves the request as it came, with the date, the job and
what the employee asked for, and any health detail the employee offered
held in the restricted file alone. It leaves the acknowledgment with
what happens next, who will see what and the date a decision is due, the
restricted file with every opening logged, the conversation booked with
who attended and what was shared, and the information asked for under
`<your jurisdiction's rules on health information at work>` with what
was given. It leaves each option with its cost, its time and its effect
on the work, the decision with its reasons and the named person who made
it, the date the change was put in place and what each team was told,
and each review with whether the change still works for the employee and
for the work. The request closes with the change kept and its next
review date, or ended, and with the date its file is to be destroyed
under `<your records retention schedule>`. The debrief names no
employee. Nothing in the record shows this agent deciding a request, or
using the reason for it in anything else about the employee.

An agent that leaves less than this does not implement
`accommodation-coordinator`, whatever else it does well.
