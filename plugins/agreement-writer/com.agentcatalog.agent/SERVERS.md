# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the contract system | write | Drafts at versions, the schedules and the executed copy live here. |
| the pricing model | read | Cap: the margin floor, set by the adopting organization. |
| the approval system | write | Every concession is recorded against the person who cleared it before it was offered. |
| the partner record | write | The terms other processes rely on are written back at the version that was signed. |
| the shared workspace with the partner | write | The draft goes out at a version and the markup comes back against that version. |

There is deliberately no grant over the signing service. This agent
prepares the paper and a person signs it.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
