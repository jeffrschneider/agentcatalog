# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the test environment | write | Test systems and test accounts on both sides, before any real data moves. |
| the partner's systems | read | Cap: set by the adopting organization. |
| the obligation register | write | The technical obligations the agreement created, closed by evidence rather than by assertion. |
| the partner record | write |  |
| the contract system | read | What the signed agreement actually obliges. |
| the notification channel | write |  |

There is deliberately no grant to move customer data to the partner.
That waits on a written transfer finding and a named person's signature.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
