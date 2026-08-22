# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the shared plan location | write | The plan and every amendment at a version both sides read from the same place. |
| the budget record | read | What our side of the plan costs, held against the line it is paid from. |
| analytics | read | Last year's result, and the values behind each measure the plan names. |
| the CRM | read | The accounts and segments the plan puts on the list. |
| the partner record | read | The agreement, the tier, and the plan the partner is working under now. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
