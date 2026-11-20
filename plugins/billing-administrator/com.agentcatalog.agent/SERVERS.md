# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the billing system | write | Each invoice built, checked, numbered, issued and sent, and each credit note and replacement drafted and then issued once approved, with no right to edit an issued invoice or to approve an invoice or a credit note. |
| the order system | read | Each booking at the version the finance approver signed. |
| the usage record | read | Each period's metered usage against the entitlement. |
| the contract repository | read | The billing terms of each agreement, and the records a disputed invoice is recomputed from. |
| the dispute register | read | Each claim and the invoice version frozen while it is argued. |
| the receivables ledger | write | Each issued invoice and credit note. |
| the general ledger | write | Each issued invoice and credit note. |
| the e-invoicing channel | write | Each invoice sent where the customer receives it that way. |
| each customer's procurement portal | write | Each invoice sent where the customer asked for it there. |
| the verified bank record | read | The company's bank details printed on each invoice. |
| the notification channel | write | The billing lead is told of each invoice that needs a person and of each billing date missed. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
