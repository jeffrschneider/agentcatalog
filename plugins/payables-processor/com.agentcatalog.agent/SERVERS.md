# The systems this abstract agent needs

Eleven systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the ERP | write | Each invoice as captured, coded and marked ready to pay, each payment run as proposed, the payment file built from the approved run, and each item marked paid, with no right to approve an exception or a run, or to release a payment. |
| the invoice inbox | read | Each invoice and credit note as it arrives. |
| the supplier portal | read | Each invoice a supplier sends through the portal. |
| the purchasing system | read | Each order and the receipts recorded against it. |
| the verified bank record | read | The bank details each payee's payment is built to. |
| the bank portal | read | The bank's report each employee's payment is matched to, with no right to move or release money. |
| the general ledger | write | Each invoice, each claim and each run posted in its period, with the totals agreed to the approved run. |
| the expense tool | write | Each claim's payment shown to the employee, and each receipt and approval kept. |
| the payroll system | write | The part of a claim treated as pay, passed before the cutoff of its pay period. |
| the document archive | write | Each invoice and its evidence, kept for the retention period. |
| the notification channel | write | A supplier is told what to correct through the contact on its record, each payee is sent its remittance advice, and the person who can clear a held item is told why it waits. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
