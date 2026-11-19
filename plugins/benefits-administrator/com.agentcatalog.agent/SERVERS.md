# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the benefits system | write | The plans, the rates, the employee costs and the eligibility rules for each plan year, and each employee's elections, dependents and benefits record. |
| the HR system | read | Each employee's eligibility facts, such as the hire date, the location and the terms of employment, and the life events recorded. |
| the payroll system | write | Each new, changed, paused or ended deduction and the payday it starts, with no right to change pay. |
| each carrier's enrollment channel | write | Each enrollment file, coverage date and end date sent, and each carrier's confirmation and bill read back. |
| the restricted evidence store | write | The evidence a plan requires, held where only the named benefits people may open it and deleted when the retention rule allows. |
| the employee portal | write | Each employee's options, costs, deadlines and confirmation of cover. |
| the notification channel | write | The enrollment figures reach the broker with no one's health identified, each reminder reaches the employee, and a mismatch reaches the benefits lead. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
