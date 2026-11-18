# The records this abstract agent must leave

This is the contract. An agent implementing `valuation-analyst` leaves
the following behind, on every run.

Each quarter leaves the measurement date, every holding the fund carried
on it and the policy version in force. Each holding has one file with
the method and the reason for any change from last quarter, the
calibration to the entry or latest round price, every input with its
source and its date, every judgment, the company's value, the allocation
through the preferences to the fund's shares, the proposed mark, and the
change from last quarter explained. A holding whose company did not
report is named as stale in the first line of its file. The outside
adviser's range, the deal lead's view and the CFO's review points sit in
the file beside how each was answered, and the committee pack records
which judgments the committee was asked to test. The approved mark is
kept at the version the committee approved and is tied to that approval
when it is posted, and an event after the measurement date is recorded
on its own. The handoff to the quarterly report gives the marks, their
movements and the plain reason for each, and the debrief compares
earlier marks with the prices later realized. A write-off leaves the
evidence that nothing is left, the zero mark with the last mark it
replaces, the event that realized the loss with its evidence and the tax
adviser's agreement, and a tax file with the fund's cost. At year end it
leaves the support for each tested mark as written at the quarter it was
set, and any moved mark as a new version with its reason.

An agent that leaves less than this does not implement
`valuation-analyst`, whatever else it does well.
