# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the sending system | write | Messages and audiences are assembled at versions, with sending switched off. |
| the live sends | trigger | Cap: how many contacts one send may reach without asking, set by the adopting organization. |
| the asset store | read | It reads the copy and the design at the versions that were signed. |
| the consent record | read |  |
| the suppression lists | read |  |
| the contact database | read |  |
| the send record store | write | Each send lands with its audience count, its schedule and what came back. |
| deliverability monitoring | read |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
