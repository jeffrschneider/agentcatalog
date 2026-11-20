# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the revenue schedule | write | Each agreement's schedule at a version that names the decision behind each line, and each period's revenue, deferred and unbilled amounts. |
| the contract repository | read | Each signed agreement and every amendment behind a booking. |
| the CRM | read | Each booking made or changed in the period, with each field naming its clause. |
| the billing system | read | The invoices and credit notes issued in the period for each agreement. |
| the delivery and usage records | read | The services, the usage and the milestones delivered in the period. |
| the general ledger | read | The deferred and unbilled revenue balances the reconciliation reads. |
| the notification channel | write | Each judgment reaches the revenue accounting lead, each delivery owner is asked to confirm, and a delivery still unconfirmed reaches the lead. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
