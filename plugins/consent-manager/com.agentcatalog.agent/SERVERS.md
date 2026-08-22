# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the consent record | write | Every agreement and every withdrawal lands with its date and the place it came from. |
| the suppression lists | write | A withdrawal is written into every list that holds the contact. |
| the contact database | read |  |
| the sending system | read |  |
| the approved rules for the change | read | At the version they were approved at. |
| the live sends | trigger | It stops a send that would break the record. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
