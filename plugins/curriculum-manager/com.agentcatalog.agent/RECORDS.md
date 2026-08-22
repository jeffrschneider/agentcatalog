# The records this abstract agent must leave

This is the contract. An agent implementing `curriculum-manager` leaves
the following behind, on every run.

Per plan: what each role has to prove, written as testable lines at a
version, and every course traced to the requirement it covers. What each
person was excused, with the evidence behind the exemption. The
schedule, with who was expected in each session. The material at a
version and the address it sits at, with the version stamped on it. Per
session: who attended by name, who did not, the date, and the questions
asked that the material did not answer. Per assessment: each question
and exercise naming the part of the standard it tests, and any item
removed with the reason it was removed. Per gap check: what a person
needs and does not have, gap by gap, with the question that exposed each
one. Per retrain: the gap named, the date it was taught again, and who
sat it. Any change to a plan after teaching started, dated. Somebody
auditing a run can see what was taught, from which version, to whom, and
why each course exists.

An agent that leaves less than this does not implement
`curriculum-manager`, whatever else it does well.
