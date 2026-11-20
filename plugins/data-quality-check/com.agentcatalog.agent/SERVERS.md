# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the CRM | read | The records the rules are run over. |
| the validation rules | write | What the system refuses, what it warns on and what it only reports later, held at a version. |
| the reporting layer | read | The query behind a failing rule, read line by line for its own errors before the data is blamed. |
| the data warehouse | read | How many records fail, which objects, which owners, and what share of the period they are. |
| the review queue | write | The rule failures and the held fills land in one queue for the person clearing it. |
| the change log | read | What shipped, changed or was imported the week a rule first began to fail. |
| the HR system | read | Only the fields a required filing asks for, at the date the filing counts from, and the record, the import or the form that wrote each failing value. |
| the payroll system | read | The headcount and the pay totals a filing's data is agreed to. |
| the general ledger | read | The sales and purchase lines an indirect tax return is built from, with the tax code and the amount on each. |
| the billing system | read | Each customer invoice a sales line is agreed to, with the address and the tax number it carries. |
| the ERP | read | Each supplier invoice a purchase line is agreed to, with the address and the tax number it carries. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
