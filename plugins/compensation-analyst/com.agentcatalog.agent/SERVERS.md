# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the job framework | read | Each job's level and the level descriptions it is matched against, with no right to add or change a job. |
| the pay range record | read | The approved range for each level and location, with the date of the market data behind it. |
| the compensation planning system | write | The refreshed ranges proposed for approval, the cost of each budget option, each proposal's check and the running spend against each budget, with no right to approve a range or a change. |
| the salary surveys | read | The market pay data the ranges are worked from, used only under the terms of each source. |
| the pay data store | read | The pay of people in the same job, level and location, read only by this agent and the named compensation people. |
| the HR system | read | Each employee's job, level, location and the other factors the pay policy names, such as time in the job and the last rating. |
| the budget | read | The budget for pay changes outside the review, the round's promotion budget and the position's approved budget. |
| the notification channel | write | A request that is incomplete reaches its manager, and a figure that needs an exception reaches the approver it needs. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
