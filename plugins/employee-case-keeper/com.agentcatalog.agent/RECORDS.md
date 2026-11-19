# The records this abstract agent must leave

This is the contract. An agent implementing `employee-case-keeper`
leaves the following behind, on every run.

Each case leaves the concern, matter or referral as it was logged, with
its channel, its date, what it describes and whom it names, and an
anonymous concern under its case reference alone. It leaves the
acknowledgment with the date an answer was due, the restricted file with
every opening logged, the route with the person who chose it, the
hearing notes as the employee checked them, the written answer or
outcome with its reasons and the policy version it rests on, and any
appeal decision with the person who decided it. A disciplinary case also
leaves the employee's warnings still in force, the similar past cases
matched on the conduct, the clause and the circumstances `<your
disciplinary policy>` names and set out with the names withheld, the
consistency check with any difference explained in writing, and the date
the outcome stops counting with its reminder, and nothing reaches the
employee's wider record beyond what `<your disciplinary policy>` sets. A
plan leaves the plan at a version with the employee's comments, each
check-in note shared with the employee, the outcome with its reasons and
the person who decided it, and the review record told only that a plan
ran and how it ended. A dismissal case leaves the record the proposal
rests on, the like cases compared with the names taken out, each open
matter as the fact that it is open and its dates, and any appeal. Each
case closes with the date its file is to be destroyed under `<your
records retention schedule>`. Nothing in the record shows this agent
choosing a route, deciding an answer or an outcome, or finding out who
raised an anonymous concern.

An agent that leaves less than this does not implement
`employee-case-keeper`, whatever else it does well.
