# card-administrator

## issue-a-card

Takes in each request, last day or breach, checks a new request against
the card policy for whether the role needs a card, records the holder's
acceptance of the terms, orders the card at exactly the approved limit
and rules, and records its activation.

covers:
- Accept the Card Terms
- Activate the Card
- Check the Role Needs a Card
- Order the Card
- Take In the Request

## keep-each-card-as-approved

Sets each approved change in the issuer's portal exactly as approved,
matches each card's status, limits and rules to its approval, and keeps
the card register with every old value and its date.

covers:
- Match the Card to Its Approval
- Record the Card in the Register
- Set the Approved Limit in the Portal

## freeze-and-close-a-card

Freezes a card the same day a breach is recorded, closes a card at the
end of its holder's last day or when a breach decision closes it, and
hands any spend still open to the reconciliation.

covers:
- Close the Card
- Freeze the Card on a Breach
- Hand the Open Spend to the Reconciliation

## take-in-the-statement

Takes in every transaction on every card for the statement period,
checks the issuer's statement against them, and sends the checked
balance to the payment run by its due date.

covers:
- Check the Statement Against the Transactions
- Send the Statement for Payment
- Take In the Statement

## chase-receipts-and-reasons

Tells each holder which transactions still need a receipt, a reason or a
cost center, chases each missing one on a schedule and then with the
holder's manager, and keeps personal spend open until it is repaid.

covers:
- Ask Each Holder for Receipts and Reasons
- Chase the Missing Receipts
- Recover Personal Spend

## reconcile-the-card-account

Confirms that each approved transaction reached the ledger at its
account, cost center and tax code, and reconciles the card account to
the statement and the ledger with each difference explained and an entry
proposed for it.

covers:
- Confirm the Spend Reached the Ledger
- Reconcile the Card Account

## record-what-the-program-taught

Records how long each card took to issue, which requests were refused
and which breaches were recorded, which holders missed receipts, and how
long each period took to close.

covers:
- Record What the Period Taught
- Record What the Request Taught
