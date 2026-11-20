# The systems this abstract agent needs

Four systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the knowledge base | write | Each article published at its version with its owner and its review date once its owner approved it, each article it replaces taken down with its address and every link moved, and the list of content the agents may answer from, with no right to approve an article or change one its owner approved. |
| the support system | write | Each saved reply published at its version, marked for who may send it and for approval each time it is used, each version it replaces taken out of use, and the cases read for the questions and gaps they show, with no right to send a reply to a customer. |
| the release calendar | read | What each release changes, for which plans and accounts, and in what order it reaches them. |
| the notification channel | write | Each owner told when content comes off the list or a decision is due, the support team told what changed, the ranked gaps sent to the knowledge lead, the head of support and the report of what customers say, each product problem passed on, and what will not be ready for a release sent to the head of support. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
