# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the account record | read | The fields the carve rule is cut on. |
| the CRM | read | What each account buys today. |
| the reporting warehouse | read | What the patches closed before. |
| the territory map | write | The candidate maps and the fixed one. |
| the model store | write | The carrying model and its assumptions. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
