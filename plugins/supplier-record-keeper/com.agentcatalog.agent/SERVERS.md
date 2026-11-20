# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the ERP | write | Each supplier record at its versions with every field's evidence, each held change, and new bank details applied only after a named approver has approved them, with the old details kept and no right to approve a record or a change. |
| the supplier portal | write | The one request for a new supplier's details, and each change request that arrives through it. |
| the payables inbox | read | Each change request as it arrived, with its headers and attachments. |
| the contract record | read | The payment terms the signed agreement sets for a new supplier. |
| the notification channel | write | The requester is told the record is open, and the supplier is told through the contact on its record where invoices go and when its bank details changed. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
