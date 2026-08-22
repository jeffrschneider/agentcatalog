# The records this abstract agent must leave

This is the contract. An agent implementing `account-monitor` leaves the
following behind, on every run.

For each question it answers, it records the account, what was asked,
the answer, the date, and every system it read with the value it found
and when that value was current. A milestone answer names the milestone
list at its version and says which of those milestones the account has
met. A risk signal is recorded whichever way it was judged, with the
reading that settled it. Anything it could not read is recorded as
unread instead of being left out of the answer.

An agent that leaves less than this does not implement
`account-monitor`, whatever else it does well.
