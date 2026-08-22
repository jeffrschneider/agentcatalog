# The records this abstract agent must leave

This is the contract. An agent implementing `deal-desk-reviewer` leaves
the following behind, on every run.

Per request: the ask as the seller wrote it, the deal it belongs to, the
level read off the published table, the time that level promises, and
the hour the seller was told both. Every non-standard item written down
on its own in the words the customer used, each carrying what it risks
with the number behind the risk wherever there is one, and the person or
function that carries it. Every read as it came back, dated, with the
reason the owner gave, and every item nobody read. What was decided the
last time the same thing was asked, on which deal, by whom, and what
happened to that deal afterwards. The alternative the desk would
approve, priced beside the ask. Then per item: the decision, the reason,
the signer, and the version of the deal it was decided against, with the
approved shape or the refusal as it went back to the seller.

An agent that leaves less than this does not implement
`deal-desk-reviewer`, whatever else it does well.
