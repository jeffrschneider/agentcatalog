# The records this abstract agent must leave

This is the contract. An agent implementing `certification-check` leaves
the following behind, on every run.

Per person: the request, naming who is put forward, for which job and by
when. The parts that must be proved, each with the reason a customer
would notice it. The assessment as checked, item by item, each item
naming the part of the standard it tests, and every item removed with
the reason. The assessors, and the conflicts that were ruled out. What
the assessors were briefed on, at a version. The sitting as scheduled,
including what the person was told they may bring. A score per part,
with the evidence it was given on and the assessor who gave it, kept so
a disputed score can be reread rather than re-argued. A score set aside
for conflict is kept marked as set aside, never deleted. The signed
result, who signed it, what it covers, and the condition and expiry on
any conditional pass. The certificate with its issue date, requirement
version and expiry. Attendance by name against the list of who must be
told. The later report setting scores against what those people did.

An agent that leaves less than this does not implement
`certification-check`, whatever else it does well.
