# The records this abstract agent must leave

This is the contract. An agent implementing `credit-analyst` leaves the
following behind, on every run.

Each credit run leaves what opened it, the legal entity that will be
billed with any parent or guarantor, the payment history with its dates,
the reports and filings with their sources and the dates they were read,
the rating with the policy rule and version behind each part, and any
part the evidence cannot support named as unsupported. Beside them sit
the proposed limit, terms and security with the evidence behind each
figure, the account owner's view, the approver's decision as recorded,
the review date with the warning signs to watch, and the follow-up level
passed to collections. Each review during collection leaves what opened
it and what it found. Nothing in the record shows this agent setting,
recording or changing a limit, or holding an order.

An agent that leaves less than this does not implement `credit-analyst`,
whatever else it does well.
