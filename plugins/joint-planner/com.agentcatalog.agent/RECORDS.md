# The records this abstract agent must leave

This is the contract. An agent implementing `joint-planner` leaves the
following behind, on every run.

The targets at a version, with the person on each side who confirmed
them. The account list with the reason written on each one, and every
account removed with the conflict or the owner behind it. The inputs per
side with a name against each line, and what our side costs against the
budget line it comes from. The milestones with one owner and one date
each. The plan at a version, with every blank filled or marked open. At
review, the gaps with the reason and the person closest to each, the
decision as both sponsors announced it, and the amendment with the
changed lines marked against the version they replace. Anybody auditing
a run can read what each side promised, what it cost, and what changed
since.

An agent that leaves less than this does not implement `joint-planner`,
whatever else it does well.
