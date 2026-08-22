# spend-reconciler

## close-scope

Fixes what a reconciliation covers before any figures are pulled, which
means the accounts, the campaigns and the dates that are being closed.
Anything outside that scope stays out of the period.

covers:
- Set What the Close Covers

## record-gathering

Pulls together the two sets of records a reconciliation compares: every
invoice and statement issued for the period, and the orders behind them
with the rates that were agreed.

covers:
- Collect the Invoices
- Pull the Order Record

## line-checking

Sets each billed line against the order it came from and the delivery
that was recorded, and works the money out again from the agreed rates,
fees, taxes and discounts. Every line comes out of this with a verdict
that cites the term it was checked against.

covers:
- Check the Rates and Fees
- Match the Invoice Lines

## difference-register

Records every line that does not match, with the amount at stake on it,
and closes the ones the buy's own records already account for so that
what is left is genuinely unexplained.

covers:
- Clear the Explained Differences
- List the Differences

## issuer-queries

Takes an unexplained or wasted line back to whoever billed it, says what
is being disputed and what it is worth, and records the answer against
the line, whether that answer is a credit, a fix, a replacement or a
refusal.

covers:
- Claim Back the Wasted Spend
- Raise the Queries
- Track the Answers

## settlement-decisions

Puts what is still open in front of the people who own the money, with
the amount and the history on each line, and records what they decide to
pay, withhold or write off, along with their sign-off on the figure for
the period.

covers:
- Approve the Verified Spend
- Decide the Open Lines

## figure-distribution

Sends a settled figure to everyone who works from it, which means the
books and the reports for a verified spend, and every agent working to
an allocation when that allocation changes.

covers:
- Release the Figures
- Tell the Agents that Read the Plan

## period-summary

Works out what was actually spent over a past period from the records
and sets it beside what was committed or what another party recorded, so
both sides end up with one figure they agree on.

covers:
- Agree the Joint Numbers
- Read Last Year's Spend

## close-learnings

Files what the close turned up for the next one, such as which lines and
which issuers are worth checking first.

covers:
- Record What Was Learned
