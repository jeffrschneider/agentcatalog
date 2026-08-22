# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the agreement store | write | The agreement at its signed version, its notice date, and the next term once it is signed. |
| the entitlement record | read | What was bought, at the level it was signed at, with every amendment. |
| the usage record | read | So a position is never argued from memory. |
| the support system | read | What is still open against the account. |
| the CRM | write | The position, the conversation and the outcome. |
| the billing system | write | The signed term recorded where it is billed, line for line against the signature. |
| the renewal brief store | write | One record the conversation runs from. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
