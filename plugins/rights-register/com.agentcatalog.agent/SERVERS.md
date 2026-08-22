# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the rights record | write | Each source lands with what it covers, its channels, its territories, its dates and the document behind it. |
| the license documents | read |  |
| the appearance releases | read |  |
| the asset store | read | It reads every version and edits none of them. |
| the CMS | read | What is live, so the agent can find published work resting on a license. |
| the content inventory | read |  |
| the notification channel | write | The agents that own a piece are told when a license behind it is running out. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
