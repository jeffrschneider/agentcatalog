# The systems this abstract agent needs

Three systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the asset store | write | Assets land at versions, in every required size. |
| brand guidelines | read |  |
| licensed image sources | read | Within the licenses the organization actually holds. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
