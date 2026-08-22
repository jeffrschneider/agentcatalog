# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the standard terms and the approved fallbacks | read | The template version in force and what is already pre-approved. |
| the clause record | write | What was decided last time the same change came up, and what this run decided. |
| the contract system | write | The markup, its version, and the copy it was made from. |
| the approval system | read | Which off-template term is signed for, and by whom. |
| the shared workspace with the buyer | write | The counter-markup and the summary that goes back with it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
