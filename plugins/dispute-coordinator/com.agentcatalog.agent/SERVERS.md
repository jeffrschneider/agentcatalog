# The systems this abstract agent needs

Twelve systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the statement store | read | The statement at the version the claimant holds, not at a corrected one. |
| the commission ledger | read | The line under dispute and the run version behind it. |
| the plan record | read | The plan at the version the claimant signed. |
| the system of record | read | The booking, the dates and the credit rule the number rests on. |
| the dispute register | write | The claim, its class, its promised date, its evidence, its answer and its cause. |
| the notification channel | write | The acknowledgement, the answer, and any date that moves before it passes. |
| the billing system | write | The invoice under dispute frozen at its version, with no right to change a line or to issue a credit note. |
| the order system | read | The booking at the version the invoice was built from. |
| the usage record | read | The readings with their dates behind a line billed on use. |
| the contract repository | read | The agreement and the clause that governs the disputed line. |
| the CRM | read | The account owner and the delivery lead to be heard on what was promised and delivered. |
| the support system | write | The holder of a claim support handed over, and the date its answer will come, put on the customer's case, with no right to answer or close the case. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
