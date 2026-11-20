# The systems this abstract agent needs

Five systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the survey tool | write | Each period's questions at their version, each survey sent once with at most one reminder, each answer joined to its case, and each specialist's own results shown only to that specialist and their team lead, with no right to change a question the head of support has not approved. |
| the support system | read | Each case that closes in the period with its channel, its topic, its account, its kind and the specialist and team that held it. |
| the consent record | read | Whether the customer may be asked on the channel, as the consent-manager agent checked it. |
| the CRM | read | The account each case belongs to, and whether it is closed. |
| the notification channel | write | Each low score and each comment that names a problem sent to the team lead with the case beside it, and the period's scores sent to the head of support, the team leads and the report of what customers say. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
