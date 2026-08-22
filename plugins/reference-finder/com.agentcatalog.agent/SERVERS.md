# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the reference register | write | The agreements, the asks and the clock live there. |
| the CRM | write |  |
| the calendar and the meeting tool | write |  |
| the support history, the renewal record and the contract store | read | To check an ask is welcome before it is made. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
