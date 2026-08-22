# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the program plan and its schedule | write | Each program's design, its dates and its current state live here. |
| the contact database | read | It reads the state and changes nothing. |
| the sending system | read |  |
| the consent record | read |  |
| analytics | read |  |

There is deliberately no write into the contact database or the sending
system. This agent decides what has to change, and the audience-operator
agent makes the change.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
