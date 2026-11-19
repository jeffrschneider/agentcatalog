# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the performance review system | write | Each cycle and round, the forms at their versions, the self-reviews, the peer feedback, each draft with its flags, the packs, the final ratings and promotion decisions at versions, the employee's response and the objectives. |
| the HR system | read | The people in each cycle, their managers, and the dates of any approved leave without its reason. |
| the job framework | read | The expectations of each level at their version, which every promotion case is read against. |
| the decision record | read | The ratings the calibration panel agreed and the promotion panel's decisions, with their reasons and any dissent. |
| the calendar | write | The date for each step of a cycle and a round. |
| the notification channel | write | Each request and reminder reaches its employee, peer or manager, and a missed date reaches the manager. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
