# The systems this abstract agent needs

Three systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access |
|---|---|
| analytics platforms | read |
| ad platforms | read |
| the CRM | read |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
