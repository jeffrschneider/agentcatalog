# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the requirement record | write |  |
| the CRM | write |  |
| the notes store | read | The confirmed discovery notes are the source. |
| the policy register and the product roadmap | read | To see which requirements cannot be met before shaping reads the record. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
