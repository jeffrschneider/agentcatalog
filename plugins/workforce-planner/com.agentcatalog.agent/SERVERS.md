# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the workforce plan | write | Each team's positions, levels, start dates and labor cost at a version, the signed positions with their budget lines, and the hiring needs added from a succession review. |
| the HR system | write | The teams, roles, levels and reporting lines it reads, and the approved plan and each signed position written to it, with no right to change an employee's record. |
| the financial planning system | read | The business plan and the labor cost budget each plan, position and option is costed against. |
| the job framework | read | The levels each position is drafted at. |
| the pay range record | read | The range for each level and location that every cost is worked from. |
| the applicant tracking system | write | Each signed position handed to the recruiter with its job, level and range. |
| the notification channel | write | A request that is incomplete or outside the plan reaches the hiring manager or the department head, and a due date at risk reaches the head of HR. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
