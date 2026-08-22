# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the program run record for each customer | write | Every step the customer was given, the date it was given and what happened after it. |
| the program's live steps | trigger | Cap: which steps it may set in motion for one customer without asking, set by the adopting organization. |
| the commitment record | write | What was promised to the customer, who promised it, and when it is due. |
| the task queue for the people who make contact | write | Cap: whose queues it may put work into, set by the adopting organization. |
| the sending system | read |  |
| the contact database | read |  |
| the CRM | read |  |
| the consent record | read |  |
| analytics | read |  |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
