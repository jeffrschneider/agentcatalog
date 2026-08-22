# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the customer and revenue record | read | The accounts, what they bought, what they renewed, and when they left. |
| the CRM | read |  |
| analytics platforms | read |  |
| ad platforms | read | What each channel has cost and returned. |
| licensed market data | read | Within the subscriptions the organization actually holds. |
| the model store | write | Each model lands at a version with the data it was fit on and the assumptions it rests on. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
