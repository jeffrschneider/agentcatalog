# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the order system | read | What was sold, on what terms, starting when. |
| the CRM | write | The account picture, the people and the handover itself. |
| the contract repository | read | What the customer actually bought. |
| the handover record | write | The package, its score and its gaps. |
| the delivery system | write | What the new owner takes on. |
| the calendar | write | The first working session in diaries on both sides. |
| the customer communication channel | write | One introduction, through the channel the customer actually uses. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
