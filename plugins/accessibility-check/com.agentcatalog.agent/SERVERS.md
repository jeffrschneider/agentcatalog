# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the accessibility and technical standards the organization has adopted | read | At their versions. |
| the staging site | read | It scores the page as it will be served. |
| the asset store | read |  |
| the review record | write | The scores land where the signers and the producing agents read them. |
| the knowledge base | read | Each help article draft at its version, scored as customers will read it once it is published. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
