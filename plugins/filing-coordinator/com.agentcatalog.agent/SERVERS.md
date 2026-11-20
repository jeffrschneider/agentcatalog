# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the compliance calendar | write | Every filing, return, notice and year-end deadline in each location, with its form, its signer and its lead time. |
| the HR system | read | Only the fields a filing's form asks for, at the date the filing counts from. |
| the payroll system | read | The reconciled year's figures and the year-end statements the returns are checked against, and only the fields a filing's form asks for. |
| each authority's filing route | write | Files a return or a filing a named person has signed, with no right to sign one. |
| the audit log | write | Each audit, each request with its due date and owner, what was sent, each follow-up and each finding. |
| the document store | write | Each filing at its version, its receipt, the filed copy, the data it was built from and each response sent. |
| the notification channel | write | A deadline the timetable shows will be missed reaches the payroll manager, the finance controller or the HR operations lead as soon as it shows. |
| the tax calendar | write | Every tax return and payment in each jurisdiction, with its entity, its period, its form, its due date, its signer and its lead time, and each refund until it arrives. |
| the tax notice log | write | Each notice from a tax authority with every date, what was sent and the receipt that closed it. |
| the tax audit log | write | Each tax audit, each request with its due date and owner, each response sent and each proposed adjustment. |
| each authority's correspondence route | write | Sends a response to a notice or an audit once a named person has approved it, with no right to approve one. |
| the bank portal | read | The bank's confirmation of each tax payment, kept with the receipt and the filed copy, with no right to release a payment. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
