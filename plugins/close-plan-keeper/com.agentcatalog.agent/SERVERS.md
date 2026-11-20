# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the close plan record | write | Every step, its owner, its date and every date that moved. |
| the CRM | write | The plan's state against the opportunity. |
| the contract system | read | The agreed text the conditions are checked against. |
| the security answer library | read | The buyer's security review worked as a dated step. |
| the buyer's vendor portal | write | Vendor forms, supplier setup, tax and banking details, and the order. |
| the shared workspace with the buyer | write | The plan and the dates both sides hold. |
| the deal pipeline | write | The closing's state against the deal, and the post-closing items with their owners and dates. |
| the cap table record | read | The capitalization as it will stand at closing, which the funds flow is built against. |
| the document store | read | The formation drafts and filings at the versions counsel released, as the evidence a step is done. |
| the close calendar | write | Every task of a month-end close with its owner, its day, its state and every day that moved, at its version. |
| the general ledger | read | Whether each sub-ledger has closed to the ledger for the period, as the evidence a close task is done, with no right to post an entry or close a period. |
| the notification channel | write | Every task owner told their cutoff and their day, and a task still late reaches the controller. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
