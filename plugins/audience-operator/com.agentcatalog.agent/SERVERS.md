# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the contact database | write | Cap: how many records one change may touch without asking, set by the adopting organization. |
| the sending system | write | A program is assembled and tested with sending switched off, at versions. |
| the live programs | trigger | A program starts sending only after the named owner says go. |
| enrichment sources | read | Within the licenses the organization actually holds. |
| the change record store | write | Every change lands here with its before-and-after counts and the copy that puts it back. |
| the approved plan for the change | read | At the version it was approved at. |
| the consent record | read |  |
| the suppression lists | read |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
