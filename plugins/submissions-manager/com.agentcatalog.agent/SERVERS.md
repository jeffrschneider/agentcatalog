# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the submissions record | write | Every body, its rules, its deadline and what came back. |
| the asset store | read | The material an entry is assembled from. |
| the claims register | read | An entry claims only what the register supports. |
| the customer and revenue record | read | The results an entry cites. |
| the meeting calendar | write | Cap: which sessions it may set without asking. |

There is deliberately no payment grant. This agent says what an entry
costs and when the money is due, and a person decides whether the
organization pays it.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
