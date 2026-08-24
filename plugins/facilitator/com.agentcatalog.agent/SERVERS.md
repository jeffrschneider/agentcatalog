# The systems this abstract agent needs

One system, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the conversation it runs | write | As a member: it sees what the members see and writes only its own signed calls, and it holds nothing else: no store, no account records, no mandate, no settlement path. What it saw is not retained after the conversation ends. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
