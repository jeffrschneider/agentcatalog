# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the community rules | read | At their versions. |
| the community platform | write | Cap: which actions it may take and for how long, set by the adopting organization. |
| the member's moderation history | read |  |
| the member messaging channel | write | The notice of what happened and how to appeal it. |
| the escalation channel | write |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
