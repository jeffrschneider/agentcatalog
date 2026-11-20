# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the card program | write | Each request, each card ordered and each change, with no right to set a limit nobody approved. |
| the card issuer's portal | write | Each card ordered, frozen, closed or set at exactly the limit and the merchant rules approved, with no right to pay the card bill or spend on a card. |
| the card issuer's statement feed | read | Every transaction on every card for each statement period. |
| the card register | write | Each card's holder, limits, merchant rules, approver, date and reason, with the old values kept with their dates. |
| the expense tool | write | Each transaction taken in and matched to its holder and to any travel booking. |
| the HR system | read | Each employee's role and manager, the address on the verified record, and a leaver's last day. |
| the general ledger | read | Each approved transaction at its account and the card account's balance. |
| the payables system | write | Each checked statement balance proposed for the payment run, with no right to approve or release it. |
| the notification channel | write | Each holder is told which receipts and reasons are due, the reminders reach the holder and then the manager, and the holder and the manager are told why a card was frozen. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
