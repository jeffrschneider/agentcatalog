# The records this abstract agent must leave

This is the contract. An agent implementing `territory-modeler` leaves
the following behind, on every run.

Per run: the carve rule as it was agreed and the fields it reads, each
candidate map with every account placed exactly once, and a carrying
number per patch naming the data it was computed from. A number that
cannot name its source is marked unsourced where a reader sees it. The
maps that lost are kept, each with the reason it lost. The fixed map
carries its version, the rule it was drawn on and the date it takes
effect, and beside every carrying number sits the assumption it rests on
and what would make that assumption wrong. Anybody auditing a run can
redraw it from what is written down.

An agent that leaves less than this does not implement
`territory-modeler`, whatever else it does well.
