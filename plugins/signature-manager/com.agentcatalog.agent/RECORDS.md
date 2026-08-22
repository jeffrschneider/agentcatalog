# The records this abstract agent must leave

This is the contract. An agent implementing `signature-manager` leaves
the following behind, on every run.

Per agreement: the executed document at a version, with each exhibit it
names marked present or missing. The signers on both sides, the
authority each signed under, and the signature date the term runs from.
The buying entity and the selling entity as matched to the entity list,
with the tax and address record for each. Every term off the standard
paper, named as non-standard, with the person who accepted it and the
date. Each promise made during the sale marked binding, carried by a
side letter, or not binding, with the clause behind every binding one.
The signature path as confirmed, and the date and version each document
went out on. What had to be corrected between signature and booking, and
which of it belongs in the next version of the paper. Somebody auditing
a run can say which version was signed, by whom, and what it obliges.

An agent that leaves less than this does not implement
`signature-manager`, whatever else it does well.
