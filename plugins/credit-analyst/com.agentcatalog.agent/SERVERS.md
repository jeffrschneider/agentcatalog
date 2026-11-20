# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the credit record | write | Each proposal with its evidence and its rating, each review date, the warning signs to watch and the follow-up level, with no right to set or change a limit or its terms. |
| the receivables ledger | read | The entity's days to pay, items past due, disputes, credit notes and any debt written off. |
| the ERP | read | The customer's record and its open orders. |
| the entity list | read | The legal entities that sign and are billed. |
| the credit reporting service | read | Outside credit reports, used only as the rules on credit information and the service's terms allow. |
| the public register of companies | read | The entity's registration and filings in each jurisdiction. |
| the CRM | read | The agreement, the account owner and what the customer plans to buy. |
| the notification channel | write | The account owner is asked for a view, and collections is told the follow-up level. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
