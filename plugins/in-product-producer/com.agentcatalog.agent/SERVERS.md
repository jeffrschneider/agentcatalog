# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the product's messaging system | write | Notices are assembled at versions, switched off. |
| the live notices | trigger | Cap: how many accounts one notice may reach without asking, set by the adopting organization. |
| the asset store | read | It reads the copy and the design at the versions that were signed. |
| the account and entitlement record | read | Which accounts have the feature the notice is about. |
| product usage data | read |  |
| the notice record store | write | Each notice lands with its audience, its dates and what came back. |
| analytics platforms | read |  |
| the suppression lists | read |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
