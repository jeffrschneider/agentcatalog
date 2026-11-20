# The systems this abstract agent needs

Ten systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the receivables ledger | write | Each receipt applied with the rule that matched it, each held amount with its reason, each customer's account and its aging, each outcome, and each write-off recorded for exactly the amount approved, with no right to clear a shortfall, move money between customers or write off a debt on its own. |
| the unapplied cash account | write | Each overpayment and each receipt with no invoice or no customer, held with its reason. |
| the bank portal | read | Each day's report of receipts and movements, with no right to move money. |
| the remittance inbox | read | Each remittance advice that came with a payment or ahead of one. |
| the customer portal | read | Each remittance a customer sends through it. |
| the billing system | read | Each open invoice, each credit note approved and not yet issued, and each dispute open against an invoice. |
| the collections tool | read | Each promise to pay with its date, everything tried on an account, and what any agency reported. |
| the decision record | read | Each decision on a held receipt and each write-off approval at its version. |
| the general ledger | read | The receivables and cash accounts the day's receipts post to. |
| the notification channel | write | The treasury-analyst agent is given the receipts expected each day and the week each open invoice is expected to be paid, and the controller is told the period's write-offs and each recovery. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
