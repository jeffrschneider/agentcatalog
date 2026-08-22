# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the asset store | write | The edit lands at a version beside the draft it edits, and never on top of it. |
| the style guide and the house standard | read |  |
| the brief and the approved outline | read |  |
| the source list the draft cites | read |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
