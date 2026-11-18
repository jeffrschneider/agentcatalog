# The records this abstract agent must leave

This is the contract. An agent implementing `mandate-check` leaves the
following behind, on every run.

Per check: the deal as proposed, with the fund, the model version and
any co-investment; each document read and its version; each investment
limit met or failed with its clause; the deal's share of commitments
alone and combined against each concentration limit; each exclusion
tested, with any doubt and who settled it; the excused investors and the
share the others would carry; the lists read, the date and any hit; the
investment period's end date and any suspension in force; each conflict
with another fund, a portfolio company or a person at the firm, with the
compliance officer's decision and any condition, in the conflicts
register; each consent with its clause, who gives it and the date it is
needed by; and the result, dated, naming every clause it rests on, with
any earlier result withdrawn when the deal changed. Where a limit could
be read two ways: both readings and the decision the chief compliance
officer and fund counsel wrote. Per co-investment: the fund's own share
against its limits, the policy and the side letter rights at their
versions, the entitled list in the policy's order, each candidate's
conflict check, the allocations with their policy lines summing to the
amount to place, and each allocation checked. Per sell-down: the plan
against the in-kind rules, any holding limit and the fund's term, and
each sale's clearance with its date and the date it lapses. Per consent:
the clause, the vote and the notice it needs, the conflict set out as
who gains and who could lose and by how much, and each condition tracked
to closed with its evidence. An auditor can take any result and reread
every clause it rests on at the version that was read.

An agent that leaves less than this does not implement `mandate-check`,
whatever else it does well.
