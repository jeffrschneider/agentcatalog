# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the flow record | write | Every field that moves, its direction, its cadence and the system that is right about it, at a version. |
| a non-live environment | write | The link is built and broken where no real record is written. |
| the systems either side | read | What each one already holds, so a flow is agreed against what is there rather than what was assumed. |
| the tool and the system of record | write | Only once the review has cleared and the link is switched on. |
| the credential store | read | The link runs under its own credentials, and this agent reads what they reach rather than widening them. |
| the stack record | read | The entry the link belongs to, and the process the tool is there to run. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
