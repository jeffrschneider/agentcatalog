# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM and the support history | read | What is already known, before the call. |
| the calendar | write |  |
| the meeting and recording tool | write | Used to record only after consent is on record. |
| the notes store | write |  |
| the CRM | write | The notes and the unanswered questions go on the record. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
