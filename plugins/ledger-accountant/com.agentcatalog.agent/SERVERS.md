# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the general ledger | write | Each manual entry, accrual journal, close journal, clearing entry and lease opening entry drafted with its support, posted only once the named approvers have approved it, and a wrong posting reversed, with no right to approve an entry or reopen a closed period. |
| the ERP | read | The goods and services received against an order and not yet invoiced, and the invoices that arrived after the last period. |
| the payroll system | read | The pay registers that `ref/hr/run-payroll` approved, for the pay owed for days already worked. |
| the commission records | read | The commission earned in the period and not yet paid, as the commission-calculator agent supplied it. |
| the lease register | read | The schedule each lease opening entry rests on. |
| the close calendar | read | The day each accrual and each close journal is due. |
| the document store | write | Each entry kept with its support and its approvals for the period the local rule on record retention sets. |
| the notification channel | write | A request with no support goes back to whoever asked, a cost with no order reaches its budget owner, and an unconfirmed or incomplete accrual reaches the reviewer. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
