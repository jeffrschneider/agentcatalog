# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the knowledge base | write | Each article drafted and revised at a version, and each change for a release held unpublished, with no right to publish an article, approve one or mark it as content the agents may answer from. |
| the support system | write | Each saved reply drafted and revised at a draft version, with no right to publish a reply or mark who may send it. |
| the product | read | Every step walked as the product behaves today, on each plan and platform an article covers, with no right to change anything in a customer's account. |
| the test environment | read | Each changed step walked before a release ships. |
| the release notes | read | What a release changes, read beside what the researcher agent gathered. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
