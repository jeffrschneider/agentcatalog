# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the system of record | read | The bookings, pulled once and frozen at a snapshot with its timestamp. |
| the plan record | read | The plan at the version each seller sits on, and the sentence behind every line. |
| the quota record | read | The quota attainment is measured against. |
| the commission ledger | write | Each component with its rate, its input and its result, and every draw and clawback with the period it came from. |
| the statement store | write | The statements, and the annotation a settled claim puts on a frozen one. |
| the payroll system | write | The file, passed with the run version and the signatures attached. |
| the notification channel | write | A seller is told what is held and why, and when a date moves. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
