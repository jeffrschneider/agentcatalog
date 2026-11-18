# The records this abstract agent must leave

This is the contract. An agent implementing `side-letter-keeper` leaves
the following behind, on every run.

Per letter: the letter at its signed version, and each clause held as an
obligation naming its owner, what sets it off, its due date and the
closed ask it came from. Per negotiation: the letters already signed for
the fund, which investors hold an MFN right that would reach each ask,
and each term of the new letter marked electable or excluded, naming the
MFN exclusion that excludes it. Per final close: the terms sent to each
MFN holder with the date its elections were due, each election received,
and each elected term added as an obligation with the date it takes
effect. Per capital call: the excused investors with the clause that
excuses each and how their share is carried by the others, and per
investor the notice period, caps, currency and delivery applied. Per fee
period: each discount, early-closer rate and waiver applied with its
clause, the offsets worked out at the share the agreement sets, and each
charge against every cap in the agreement and each letter with the
running total for the year and any excess named as the firm's. Per
quarter: each investor's reporting promises on content, template,
currency, timing and extra reports, each statement checked with any
missing item named against its clause, and any missed date recorded
against the letter it breaks. An auditor can take any clause of any side
letter and find every call, fee period and report it was checked
against.

An agent that leaves less than this does not implement
`side-letter-keeper`, whatever else it does well.
