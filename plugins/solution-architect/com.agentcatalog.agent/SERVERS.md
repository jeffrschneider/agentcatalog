# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the requirement record | read | One record, at one version. |
| the shape library | write |  |
| the product roadmap and the architecture standards | read |  |
| the security review queue | write |  |
| the CRM | write |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
