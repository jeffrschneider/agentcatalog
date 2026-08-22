# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the supplier and registration record | write | Every entry lands with its owner, its cost, its term and its renewal date. |
| the requirements record | write | The requirements and the criteria land at a version, dated before the first candidate is looked at. |
| the agreements and their terms | read | At the versions they were signed at. |
| the accounting record for the period | read | What has actually been billed against each entry. |
| the budget for the period | read | What each entry was allocated. |
| public and licensed sources | read | Within the subscriptions the organization actually holds. |
| the notification channel | write | The owner of an entry is told before its renewal date with the notice period named. |
| the review schedule | write | The date each entry comes back up. |
| the meeting calendar | write | Cap: which sessions it may set without asking, set by the adopting organization. |

There is deliberately no payment grant and no grant to enter into an
agreement. This agent says what an entry costs and when the money is
due, and the people who hold the money commit it and pay it.

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
