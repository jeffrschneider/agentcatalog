# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the purchasing system | write | Each request, each order at its versions, the supplier's acceptance, each receipt and each exception, with no right to approve a purchase or commit money. |
| the ERP | read | Each supplier's approved record, the invoices matched to each order, and the order lines coded to an asset class. |
| the budget record | read | The budget line each request names and the commitment recorded against its order. |
| the contract record | read | The agreements in force that already cover a purchase, and the signed agreement each order is placed under. |
| the decision record | read | A department's own choice of a supplier, and an approved investment case behind a purchase. |
| the notification channel | write | The requester is asked once for everything missing and told the date a held request is expected, and each order reaches the supplier through the contact on its record. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
