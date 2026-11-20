# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the control list | read | Each control as written, its owner, its test date and the result of its last test. |
| the general ledger | read | The journals, reconciliations and approvals each sample is drawn from and tested against. |
| the ERP | read | The orders, receipts, invoices and supplier changes each sample is drawn from and tested against. |
| the payment system | read | Each payment run with its approval and its release. |
| the bank portal | read | The portal's users and their rights, and the payments each user created, approved or released. |
| the expense tool | read | The claims and card transactions a sample is drawn from. |
| the HR system | read | Each person's role, and the payroll access list from `ref/hr/review-access-to-employee-data`. |
| the test record | write | Each test with its population, its draw, each item's result and its evidence, and each fix tested again. |
| the access review record | write | Each person flagged with the duties their access joins, and each item one person both prepared and approved. |
| the issue tracker | write | Each failure written up on `<your finding template>`, with no right to rate or close a finding. |
| the notification channel | write | Each finding reaches the controller and the control owner, and a failure that looks like fraud reaches the person the company names for it. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
