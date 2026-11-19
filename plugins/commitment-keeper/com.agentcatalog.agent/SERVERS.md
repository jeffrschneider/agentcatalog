# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the commitment tracker | write | Every commitment as an item with an owner, a date and a state, and every change to one. |
| the signed plan | read | The commitments as they were signed, at the version they were signed at. |
| the calendar of every signer | write | The review dates, so a review is on a calendar before the plan closes. |
| the partner record | read | Who on each side owns what. |
| the portfolio reporting system | read | Each change's measure as the company reports it, read beside the baseline at every review. |
| the calendar | write | Each check-in of a plan about one employee, on the calendars of the manager and the employee, with the date a probation closes shown where one applies. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
