# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the fund accounting system | write | The capital accounts, and every call, distribution, fee, expense, offset and carried interest allocation booked to them, live here. |
| the side letter register | read | Each investor's excusals, fee terms, notice periods, caps and reporting terms. |
| the bank portal | read | The balances and receipts the books are agreed to, with no right to release a payment. |
| the portfolio reporting system | read | The fees companies paid the firm, and the holdings the auditor confirms. |
| the cap table record | read | The holding each proceeds came from and the shares the fund holds at year end. |
| the accounts payable system | write | Each signed fee and expense entered for payment, and each bill to the firm or a company raised with its due date. |
| the audit request portal | write | Every auditor request and its answer in one dated log. |
| the notification channel | write | A late payer, a disagreement between workings or a missed date reaches the CFO the day it is found. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
