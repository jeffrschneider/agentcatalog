# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the customer and revenue record | read | The accounts, what they bought, what they renewed, and when they left. |
| the CRM | read |  |
| analytics platforms | read |  |
| ad platforms | read | What each channel has cost and returned. |
| licensed market data | read | Within the subscriptions the organization actually holds. |
| the model store | write | Each model lands at a version with the data it was fit on and the assumptions it rests on. |
| the financial planning system | read | The costs gathered for an investment case, the budget and the latest forecast, which the case's cost and return are modelled from. |
| the general ledger | read | What like spend has actually cost, as a source for the rates in an investment case. |
| the support system | read | The requests that arrived on each channel by topic and interval, which a forecast of requests is fit on and set beside. |
| the release calendar | read | The releases ahead and the dates they reach customers. |
| the marketing calendar | read | The campaigns and price changes ahead that may bring requests. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
