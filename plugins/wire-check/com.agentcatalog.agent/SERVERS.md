# The systems this abstract agent needs

Seven systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the bank portal | read | The receipts, payments and bank confirmations it matches, with no right to release or approve a payment. |
| the verified bank record | read | The fund's own receiving accounts, which every capital call notice is checked against. |
| the verified payee record | read | Each payee's confirmed account and the number on file to call back. |
| the verified investor bank record | read | Each investor's confirmed receiving account and the number on file to call back. |
| the close plan record | write | Each line of a closing's funds flow marked verified, held or confirmed received. |
| the fund accounting system | read | What was called from each investor, the approved distribution and the signed charges, which every receipt and payment is matched to. |
| the notification channel | write | A held payment or a suspected fraud reaches the CFO the same day. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
