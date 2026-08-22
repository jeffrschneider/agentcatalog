# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the content plan and its schedule | write | The piece's dates and its current state live here. |
| the asset store | read |  |
| the CMS | read | It reads what is live and changes nothing. |
| analytics | read |  |

There is deliberately no publishing grant. This agent says when the
piece goes live, and the web-producer agent is the one that publishes
it.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
