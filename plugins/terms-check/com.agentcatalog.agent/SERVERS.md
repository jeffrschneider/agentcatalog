# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the standard terms store | read | Every term scored at the version in force, and the version recorded beside the score. |
| the contract record | read | The paper the proposed terms would sit on. |
| the delegation of authority | read | Who may sign what, when a band rather than a term is being scored. |
| the deal desk queue | write | The score written back against the item it belongs to. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
