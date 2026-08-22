# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | write | The account, its people, and the openings against it. |
| the usage system | read | How close each metered thing is to what was bought, over a window rather than on one day. |
| the support system | read | An account in an open crisis is not worked. |
| the billing system | read | Collections and anything in dispute. |
| the contract record | read | The products, licences, limits and dates on the agreement they hold today. |
| the account plan | read | What the plan already says to sell here. |
| the opening register | write | The opening, its evidence, and the decision on it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
