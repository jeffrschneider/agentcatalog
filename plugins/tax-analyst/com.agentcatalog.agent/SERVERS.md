# The systems this abstract agent needs

Thirteen systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the tax workpapers | write | Each provision, return, reconciliation, position set out and adjustment worked out at its version, with no right to take a position or sign a return. |
| the general ledger | read | The tax accounts, the period's sales and purchase lines and the transactions an audit request covers. |
| the billing system | read | Each sales invoice and the tax shown on it. |
| the ERP | read | Each purchase line with its tax code, and the records an audit request covers. |
| the consolidation system | read | Each entity's results before tax and its signed accounts. |
| the asset register | read | The fixed asset detail each income tax return needs. |
| the payroll system | read | The pay totals each income tax return needs. |
| the record of filed returns | read | Each return as filed with its receipt and its workpapers, for a notice or an audit. |
| the bank portal | read | The tax and the instalments already paid, with no right to prepare or release a payment. |
| the tax calendar | read | Each return's due date and named signer. |
| each tax authority's published contact and payment details | read | The account each payment is set out to, and the details a notice is checked against. |
| the document store | write | Each response, each correction set out and each record sent, with what was held back and why. |
| the notification channel | write | Each change in a rule reaches the head of tax, each judgment and position reaches its decider, and a gap in the records reaches the person who holds the fact. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
