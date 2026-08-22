# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| analytics platforms | read |  |
| ad platforms | read |  |
| the CRM | read |  |
| the plans and commitments for the period | read | What each run said it would do. |
| the report store | write | Each period's report lands at a version. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
