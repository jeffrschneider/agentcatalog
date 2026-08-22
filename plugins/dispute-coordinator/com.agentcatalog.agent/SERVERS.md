# The systems this abstract agent needs

Six systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the statement store | read | The statement at the version the claimant holds, not at a corrected one. |
| the commission ledger | read | The line under dispute and the run version behind it. |
| the plan record | read | The plan at the version the claimant signed. |
| the system of record | read | The booking, the dates and the credit rule the number rests on. |
| the dispute register | write | The claim, its class, its promised date, its evidence, its answer and its cause. |
| the notification channel | write | The acknowledgement, the answer, and any date that moves before it passes. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
