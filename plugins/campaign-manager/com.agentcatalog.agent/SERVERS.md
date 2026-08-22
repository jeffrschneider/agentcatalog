# The systems this abstract agent needs

Three systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| scheduler | write | Publishing fires only after the launch decision. |
| analytics | read |  |
| the asset store | read |  |

There is deliberately no budget grant. This agent proposes the number
and a person confirms it, which is an escalation rather than an access.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
