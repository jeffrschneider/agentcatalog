# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the usage record | read | Where use fell, when, and for which team. |
| the support system | read | Open tickets and anything in dispute. |
| the billing system | read | Unpaid invoices, and what is in collections. |
| the CRM | read | Which named contacts are still there and which have left. |
| the agreement store | read | The notice date the clock is set against. |
| the risk record | write | The reason, the severity and the outcome. |
| the notification channel | write | The owner is told inside the time the policy sets. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
