# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the decision record | write | Each decision lands at a version with its answer, its reasons and its dissent. |
| the evidence store | read | What the gathering agents filed for this decision. |
| the standards and governing documents the decision must follow, at their versions | read |  |
| the plans and commitments the decision has to sit inside | read |  |
| the meeting calendar | write | Cap: which meetings it may set without asking, set by the adopting organization. |
| the notification channel | write | The answer reaches every agent that acts on it. |
| the review schedule | write | The date each recorded answer comes back up. |
| the deal pipeline | write | A deal's stage and the committee's decision on its record, where the next deal team can read it. |
| the HR system | write | Each change a pay review approved, handed to the employee's record with its approver and its effective date, with no right to change any other field. |
| the delegation of authority | read | The approvers a budget, a reforecast, an investment case, a choice of supplier or a write-off needs at the version in force, which every such decision is put to and checked against. |
| the financial planning system | read | The budget, the reforecast and the investment case at the versions put to the approvers. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
