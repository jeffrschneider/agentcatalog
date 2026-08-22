# The records this abstract agent must leave

This is the contract. An agent implementing `requirements-recorder`
leaves the following behind, on every run.

One line per requirement, quoted in the buyer's words, with any
paraphrase marked as a paraphrase, the person who asked for it, and the
date they asked. The needs-and-wants split, with who drew the line. The
contradictions found, and what came back when each went to the buyer.
The buyer's ranking, recorded as the buyer's, with any seller re-ranking
kept beside it as a separate marked opinion. The requirements marked as
unmeetable, each with its reason and the date it was marked. The
read-back and the buyer's confirmation. The version number and its date,
with earlier versions still readable, and every later requirement
written, attributed and versioned in rather than absorbed quietly. The
mapping of shape to record, showing each requirement met, deferred or
refused.

An agent that leaves less than this does not implement
`requirements-recorder`, whatever else it does well.
