# The systems this abstract agent needs

Three systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the asset store | write | Cuts land at versions, per platform. |
| brand guidelines | read |  |
| licensed footage and music sources | read | Within held licenses. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
