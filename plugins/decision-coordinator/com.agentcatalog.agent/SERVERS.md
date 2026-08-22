# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the decision record | write | Each decision lands at a version with its answer, its reasons and its dissent. |
| the evidence store | read | What the gathering agents filed for this decision. |
| the marketing standards at their versions | read |  |
| the plans and commitments the decision has to sit inside | read |  |
| the meeting calendar | write | Cap: which meetings it may set without asking, set by the adopting organization. |
| the notification channel | write | The answer reaches every agent that acts on it. |
| the review schedule | write | The date each recorded answer comes back up. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
