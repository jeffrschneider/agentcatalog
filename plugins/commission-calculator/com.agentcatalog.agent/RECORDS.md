# The records this abstract agent must leave

This is the contract. An agent implementing `commission-calculator`
leaves the following behind, on every run.

Per run: the period boundaries, the sellers in scope, the plan version
each seller sits on, and the booking snapshot with the system, the query
and the timestamp it was taken at. Every booking against its seller, its
territory and its plan version, with every unmatched booking listed
rather than dropped and every incomplete one naming the field it is
missing. The credited amount per seller per booking with the split rule
that produced it, attainment with the quota it was measured against,
each component with its rate and its input beside its result, and every
gate, accelerator and cap marked applied or not applied. Every draw,
recoverable and clawback with the period it came from, and every held
amount with the condition it waits on and the period it is expected in.
Each statement built so that every line names its booking, its rate, its
plan sentence and its date. Then what each manager accepted and what
they said was wrong, the run at a version with its total and its
signatures, what payroll received and when, and every correction with
the plan sentence or the record that caused it.

An agent that leaves less than this does not implement
`commission-calculator`, whatever else it does well.
