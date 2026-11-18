# The records this abstract agent must leave

This is the contract. An agent implementing `subscription-reviewer`
leaves the following behind, on every run.

The close as taken in: its date, whether it is the first, a later or the
final close, the investors joining and the commitment each stated. Per
investor: the completeness check naming every page, form, signature and
tax form, and the commitment on the documents set beside the commitment
stated; the one list of missing items sent, with its date and the date
the items arrived or did not; the eligibility finding naming the
offering rule the investor qualifies under, its tax position, any
benefit plan status and the evidence of the signer's authority; the
screening result as read, with the chief compliance officer's clearance
of any hit; and the acceptance as the GP gave it, in whole, in part with
the cut and the allocation rule it came from, or a refusal with its
reason in the terms of the offering rules. The close clock with each
warning raised and to whom. The filed close record, with the signed
documents, the investor register, the screening results and the
acceptances. Any admitted investor can be traced from its stated
commitment to its signed acceptance and the evidence that it was
eligible.

An agent that leaves less than this does not implement
`subscription-reviewer`, whatever else it does well.
