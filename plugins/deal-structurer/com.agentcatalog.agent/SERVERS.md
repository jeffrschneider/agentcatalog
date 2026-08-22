# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the financial model | write | The economics, the assumptions and the downside case. |
| the contract system | write | The term sheet and the drafts, at versions. |
| the approval system | write | The mandate and the approvals the shape depends on. |
| the obligation register | write | What the signed terms owe, written out as work with owners and dates. |
| the partner record | write |  |
| the pricing policy and the standard partner terms | read | The terms the company already stands behind, so a new one is a deliberate choice. |

There is deliberately no grant on the signature system. Signing is a
human gate.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
