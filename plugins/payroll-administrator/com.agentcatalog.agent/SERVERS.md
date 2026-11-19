# The systems this abstract agent needs

Nine systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the payroll system | write | Each period's changes, deductions, pay, register and payment file, the year's totals and statements, and the new year's rates once the payroll manager confirms them, with no right to approve a register or release a payment. |
| the HR system | read | The approved changes and the manager named to approve each employee's time and variable pay. |
| the time and attendance system | read | The hours, overtime and shift premiums for the period. |
| the benefits system | read | Each employee's benefit deductions and the date each starts or stops. |
| the verified bank record | read | The account each employee's payment is built to. |
| the general ledger | write | Each period's journal for pay, tax, contributions and deductions, and the totals the year is reconciled to. |
| the employee portal | write | Each payslip on payday and each year-end statement by its deadline. |
| each tax authority's filing channel | write | Each period's withholding paid and filed by its date with the payroll manager. |
| the notification channel | write | A change held past the cutoff reaches the person who sent it, and a due date at risk reaches the payroll manager. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
