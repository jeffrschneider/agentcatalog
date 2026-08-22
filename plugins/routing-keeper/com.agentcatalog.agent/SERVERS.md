# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the system that delivers the work | write | The rule runs where work is handed out. |
| the CRM | write | A misrouted record is reassigned with its reason. |
| the rule register | write | Every rule at its version, with the cases filed against it. |
| the published rule page | write | The copy people are held to. |
| the announcement channel | write | Who is told what changed. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
