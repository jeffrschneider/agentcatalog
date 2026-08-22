# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the close plan record | write | Every step, its owner, its date and every date that moved. |
| the CRM | write | The plan's state against the opportunity. |
| the contract system | read | The agreed text the conditions are checked against. |
| the security answer library | read | The buyer's security review worked as a dated step. |
| the buyer's vendor portal | write | Vendor forms, supplier setup, tax and banking details, and the order. |
| the shared workspace with the buyer | write | The plan and the dates both sides hold. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
