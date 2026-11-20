# The systems this abstract agent needs

Thirteen systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the treasury system | write | Each day's position, each week's forecast, each transfer and funding as prepared, each placement and its maturity, and each transfer and funding recorded, with no right to approve or release a payment. |
| each bank's portal | read | Each account's balance and movements, each bank's report, and the bank's own list of signers, users and limits. |
| the bank account record | write | Each account with its signers, its releasers and their limits, changed only after the approval and the bank's confirmation are on the record. |
| the ERP | read | The approved supplier invoices, the open orders and the proposed payment runs by the day each falls due. |
| the payroll system | read | The pay calendar and each approved register's total and payday. |
| the general ledger | write | The entries for each transfer and funding that was approved and released, and the balance each entity owes the other after a transfer between them, with no right to approve a journal. |
| the facility record | write | Each loan and facility with its dates, its covenants, its definitions and every amendment, and each test with its workings, its certificate and the lenders' acknowledgment. |
| the planning system | read | The latest reforecast at its version, for the later months of the forecast and the covenant projection. |
| the consolidation system | read | The closed and signed-off figures each covenant test reads. |
| the HR system | read | A leaver or a mover who holds authority at a bank, with the last day. |
| the delegation of authority | read | The releasers `<your dual control rule>` needs on each account. |
| the signature system | trigger | The bank's forms and the compliance certificate sent to the named signers, with no right to sign for any of them. |
| the notification channel | write | The position reaches the treasurer by `<your cutoff time>`, a shortfall or a covenant at risk reaches the CFO, and the payroll manager hears that the payroll account is funded. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
