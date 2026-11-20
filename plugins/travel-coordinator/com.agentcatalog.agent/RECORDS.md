# The records this abstract agent must leave

This is the contract. An agent implementing `travel-coordinator` leaves
the following behind, on every run.

Each trip leaves the request with its business reason and its cost
center, the reading against the policy at its version, the manager's
approval where the policy asks for it, the options offered with the
lowest that fit first and their cancellation terms, the traveler's
choice, and any exception with the traveler's reason and the approver's
written decision dated before the booking. Beside them sit each booking
with its reference, its fare and its terms, the itinerary as sent, each
change or cancellation with the approval behind it, and each cost passed
to the expense record. The trip closes with each unused ticket and
credit recorded for later use and the date the whereabouts were deleted.
Nothing in the record shows this agent booking outside the policy
without a written approval, booking a different fare or a higher price
than the one chosen or approved, or using the whereabouts for anything
other than reaching and helping the traveler.

An agent that leaves less than this does not implement
`travel-coordinator`, whatever else it does well.
