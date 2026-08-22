# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the opportunity record | write | The answers, the gaps and the decision live there. |
| the CRM | write |  |
| product usage data, the support system and contract records | read | The account is read again for what changed since the inquiry. |
| the nurture list | write | A returned lead goes back with its reason and its date. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
