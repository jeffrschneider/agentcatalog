# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the audit portal | write | Each approved answer sent by its due date, and the log of what went, when, to whom and at which version. |
| the general ledger | read | The figures each answer is tied to, and the closed trial balance. |
| the ERP | read | The orders, invoices and records behind an answer. |
| the close records | read | The reconciliations and schedules behind an answer, each at its version. |
| the answer library | read | The approved answers each draft starts from. |
| the issue tracker | read | Last year's points and the state of each fix, and each fix this year's letter calls for. |
| the document store | write | The request list, the adjustment list, the representation letter as drafted, and the auditor's signed opinion filed with the statements it covers. |
| the signature system | trigger | The representation letter sent to the named officers, with no right to sign for any of them. |
| the notification channel | write | Each request reaches its owner with its due date, a date at risk reaches the controller, and each proposed adjustment reaches the controller and the CFO. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
