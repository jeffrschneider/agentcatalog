# The records this abstract agent must leave

This is the contract. An agent implementing `tier-assessor` leaves the
following behind, on every run.

The rules at the version in force, and the date they were published. The
evidence per partner, each line naming the system and the date it was
read from, with every gap marked as a gap. The tier the rules gave, with
the inputs it was computed from, so somebody else can recompute it from
what was written down. Every exception with its reason, the person
asking, the signer, and the date it expires, counted in the published
round. In a performance round, the score with the rules version beside
it, the finding said as on plan, behind or at risk, and the referral
with the score and the date behind it. At an exit, the access that was
taken down and when. At the close, where the rules gave a tier nobody
could defend, and what the next version should say.

An agent that leaves less than this does not implement `tier-assessor`,
whatever else it does well.
