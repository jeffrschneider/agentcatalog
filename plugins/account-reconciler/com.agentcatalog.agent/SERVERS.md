# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the general ledger | read | Each account's closing balance and the period's entries, and each entity's balances and trading with the other entities. |
| the bank portal | read | The statement behind each bank account. |
| the ERP | read | The payables and receivables sub-ledgers and the schedules behind the accounts they feed. |
| the asset and lease register | read | The register's totals behind the asset and lease accounts. |
| the payroll system | read | The approved registers and the payments behind each payroll account. |
| the consolidation system | read | Each entity's balances with the other entities, translated at the rates set for the period. |
| the close records | write | Each reconciliation sheet at its version with its evidence, its preparer and the reviewer's sign-off, with no right to sign one off. |
| the notification channel | write | A missing source is asked for, a difference the evidence does not explain reaches its account owner, and an old or large item reaches the controller. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
