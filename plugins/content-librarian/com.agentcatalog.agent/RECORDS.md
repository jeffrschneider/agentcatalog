# The records this abstract agent must leave

This is the contract. An agent implementing `content-librarian` leaves
the following behind, on every run.

The inventory at a version every time it is rebuilt, with each live page
carrying what it was made to do, the date it last changed, what it is
doing now, and where every figure came from. The refresh cycle's list,
giving the reason each page is on it, and a line for the pages that were
looked at and left for a later cycle. A decision record for every merge,
retirement and redirect, naming the version that came down, what now
stands at its address, and the person who said so. A page it could not
measure is recorded as unmeasured, with the reason.

An agent that leaves less than this does not implement
`content-librarian`, whatever else it does well.
