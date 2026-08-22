# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CMS | read | Everything that is live, with the date each page last changed. |
| analytics platforms | read |  |
| the site's search performance data | read |  |
| the content inventory | write | The list is rebuilt at a version every time it is refreshed. |
| the content plan and its schedule | write | A refresh cycle's pages and their dates land beside the new pieces, on one schedule. |
| the asset store | read |  |
| the claims register | read | At its version, so the agent can find live pages resting on a claim that has since changed. |

There is deliberately no write access to the CMS. This agent decides
which pages have to change and what has to happen to them, and the
agents that own a page make the change.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
