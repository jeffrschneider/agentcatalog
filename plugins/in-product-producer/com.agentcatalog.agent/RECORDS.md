# The records this abstract agent must leave

This is the contract. An agent implementing `in-product-producer` leaves
the following behind, on every run.

The notice at a version, with a preview that shows it the way an account
will see it. The audience at a version, with the count of accounts that
have the feature, the count left after the exclusion rules were applied,
and the rule behind every removal. The run settings as they were set,
naming where in the product the notice appears, the date it starts, the
date it ends, and how often one person sees it. The go record naming the
version that went live, the time it was switched on, and the person who
said go. The takedown record naming the version that came down and the
date it came down. The report afterwards, giving the accounts that saw
the notice, the people who did what it asked, the people who dismissed
it and the people who did nothing. Anything it could not verify is
recorded as unverified instead of being left out.

An agent that leaves less than this does not implement
`in-product-producer`, whatever else it does well.
