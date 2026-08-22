# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the registration record | write | The claim at a version, with its rule results, its scope, its dates and its close. |
| the partner portal | read | What the partner submitted, as they submitted it. |
| the CRM | write | The claim attached to the deal it protects, and what has moved on that deal. |
| the agreement record | read | The clause the protection period is read off. |
| the partner record | read | The tier, the agreement in force, and anything overdue that the rules take into account. |
| the notification channel | write | The answer to both sides, and the warning before a claim lapses. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
