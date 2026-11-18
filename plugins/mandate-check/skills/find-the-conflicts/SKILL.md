---
name: find-the-conflicts
description: Checks the company, its parties, each candidate and each sale against the restricted list, finds conflicts with the firm's other funds, its portfolio companies and its own people, sets out who gains and who could lose, and brings each one to the chief compliance officer to decide. Use it when running `ref/pc/check-the-deal-against-the-fund-mandate` and 3 other reference processes.
license: CC-BY-4.0
metadata:
  agent: mandate-check
  agent-version: "1"
---

# Find the conflicts

## What it does

Checks the company, its parties, each candidate and each sale against
the restricted list, finds conflicts with the firm's other funds, its
portfolio companies and its own people, sets out who gains and who could
lose, and brings each one to the chief compliance officer to decide.

## Where it happens

The agent does this in eight activities across four reference processes.
Each one names the activity as that process words it.

- **Check Each Candidate for Conflicts**
  - `ref/pc/offer-a-co-investment`, activity 5 -
    [Offer a Co-Investment](../../../../processes/private-capital/offer-a-co-investment.md)
- **Check the Restricted List**
  - `ref/pc/check-the-deal-against-the-fund-mandate`, activity 7 -
    [Check the Deal Against the Fund Mandate](../../../../processes/private-capital/check-the-deal-against-the-fund-mandate.md)
- **Clear Each Conflict**
  - `ref/pc/check-the-deal-against-the-fund-mandate`, activity 14 -
    [Check the Deal Against the Fund Mandate](../../../../processes/private-capital/check-the-deal-against-the-fund-mandate.md)
- **Clear Each Sale with Compliance**
  - `ref/pc/sell-down-a-public-position`, activity 9 -
    [Sell Down a Public Position](../../../../processes/private-capital/sell-down-a-public-position.md)
- **Find Conflicts with Other Funds**
  - `ref/pc/check-the-deal-against-the-fund-mandate`, activity 11 -
    [Check the Deal Against the Fund Mandate](../../../../processes/private-capital/check-the-deal-against-the-fund-mandate.md)
- **Find Conflicts with Portfolio Companies**
  - `ref/pc/check-the-deal-against-the-fund-mandate`, activity 12 -
    [Check the Deal Against the Fund Mandate](../../../../processes/private-capital/check-the-deal-against-the-fund-mandate.md)
- **Find Interests of the Firm's People**
  - `ref/pc/check-the-deal-against-the-fund-mandate`, activity 13 -
    [Check the Deal Against the Fund Mandate](../../../../processes/private-capital/check-the-deal-against-the-fund-mandate.md)
- **Set Out the Conflict**
  - `ref/pc/seek-an-advisory-committee-consent`, activity 3 -
    [Seek an Advisory Committee Consent](../../../../processes/private-capital/seek-an-advisory-committee-consent.md)

## What to record

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

That contract covers every activity this abstract agent takes on, and it
is repeated in `com.agentcatalog.agent/RECORDS.md`. What the abstract
agent does not do is in `com.agentcatalog.agent/NOT.md`.
