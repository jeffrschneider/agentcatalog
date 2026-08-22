# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the website's content system | write | Pages are built as drafts, at versions, each with a preview link. |
| the website | write | Cap: which parts of the site it may publish to without asking, set by the adopting organization. |
| the asset store | read |  |
| the site's templates and components | read |  |
| redirects and address settings | write |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
