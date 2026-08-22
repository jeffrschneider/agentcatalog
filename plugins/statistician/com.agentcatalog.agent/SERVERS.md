# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the study design | read | The question, the method and the sample, at the versions they were set at. |
| the response record | read | Every response as it was given, and every response the study removed. |
| the customer and revenue record | read | The accounts, what they bought, what they renewed, and when they left. |
| analytics platforms | read |  |
| ad platforms | read | What each channel served and what came back. |
| licensed market data | read | Within the subscriptions the organization actually holds. |
| the calculation record | write | Every figure lands with the data behind it, the method used, the exclusions applied and the range around it. |

There is deliberately no write into the response record. This agent says
which responses it left out and under which rule, and the study-manager
agent keeps the responses as they were given.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
