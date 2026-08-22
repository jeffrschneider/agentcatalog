# The records this abstract agent must leave

This is the contract. An agent implementing `redline-reviewer` leaves
the following behind, on every run.

Per review: the markup at its version and the copy it was made from. One
item per changed clause, with the original text and the buyer's text
side by side, its class, and its clause number. What was decided on the
same change in past deals and who decided it. Every clause closed as
accept, counter or reject, each with its reason and the person who made
the decision. The counter-markup with every off-template term listed
separately and every approver named. The version sent back and the date.
Each further markup read against the copy we last sent, with every
difference named. The confirmed clean text, and the accepted changes
written to the record other deals read.

An agent that leaves less than this does not implement
`redline-reviewer`, whatever else it does well.
