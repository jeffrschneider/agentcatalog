# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the usage record | read | What was actually used, period by period. |
| the billing system | read | What was invoiced against what was metered. |
| the agreement store and the entitlement record | read | A use number means nothing without the limit it sits under. |
| the CRM | write | The reading against the account, dated. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
