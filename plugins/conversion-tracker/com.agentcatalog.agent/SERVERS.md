# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| analytics platforms | write | Tags and conversion definitions land at versions. |
| the CRM | write | Cap: which objects and fields it may create, set by the adopting organization. |
| ad platform conversion settings | write | The definitions the buy optimizes toward, with no access to bids or budgets. |
| the site's pages | write | Limited to measurement code. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
