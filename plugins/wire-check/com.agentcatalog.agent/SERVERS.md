# The systems this abstract agent needs

Seventeen systems, named by role rather than by product. The access
level is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the bank portal | read | The receipts, payments and bank confirmations it matches, with no right to release or approve a payment. |
| the verified bank record | read | The fund's own receiving accounts, which every capital call notice is checked against. |
| the verified payee record | read | Each payee's confirmed account and the number on file to call back. |
| the verified investor bank record | read | Each investor's confirmed receiving account and the number on file to call back. |
| the close plan record | write | Each line of a closing's funds flow marked verified, held or confirmed received. |
| the fund accounting system | read | What was called from each investor, the approved distribution and the signed charges, which every receipt and payment is matched to. |
| the notification channel | write | A held payment or a suspected fraud reaches the CFO the same day, or for a company's own payments the controller, the payables lead or the treasurer. |
| the payroll system | read | The approved register and the payment file built from it, which every payroll payment is checked against, with no right to change a line, approve a register or release a payment. |
| the verified employee bank record | read | Each employee's confirmed account and the contact already on file that a change is confirmed through. |
| the verified supplier bank record | read | Each supplier's confirmed account, the date it was confirmed and the contact on file it was confirmed through, which every supplier payment is checked against. |
| the bank account record | read | The company's own accounts that a transfer or a payroll funding may move between. |
| the treasury system | read | Each transfer and each payroll funding as prepared, with its accounts, its amount, its value date and the need or the register it meets. |
| the ERP | write | The first payment to a supplier's new account flagged for a check, and each payment in a supplier run marked checked or held, with no right to change bank details, approve an invoice or release a payment. |
| the payables inbox | read | The message that asked for a bank change, with its sender, its headers and its attachments, which is kept as evidence and never answered with the confirmation. |
| the supplier portal | read | A bank change request that arrives there, with its sender and its date. |
| the signed agreements | read | A supplier's contact found apart from the request, in the agreement it signed. |
| company registry sources | read | A supplier's contact found apart from the request, on the public record. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
