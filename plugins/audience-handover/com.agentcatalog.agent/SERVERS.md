# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the approved list | read | At the version it was approved at. |
| the consent record | read |  |
| the suppression lists | read |  |
| the agreement covering the transfer | read | Which fields may be sent, what they may be used for, and how long the receiving organization may hold them. |
| the destination system | write | Cap: which fields may leave and how many records one transfer may carry, set by the adopting organization. |
| the transfer record | write | Every transfer lands with what was sent, what was accepted and what matched. |
| the notification channel | write |  |

There is deliberately no grant to build or change a segment. This agent
sends the list it was handed at the version it was approved at, and the
audience-operator agent is the one that builds a list in the first
place.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
