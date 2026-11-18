# The systems this abstract agent needs

Eight systems, named by role rather than by product. The access level is
the most this work needs, and a deployment that grants more is granting
more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| the deal pipeline | write | The sector proposal, the map at each version, and each opportunity opened with its named owner. |
| the customer relationship management system, or CRM | write | Past meetings, passes and owners read before a company is scored or approached, and the outcome written back. |
| company data sources | read | Where every listed company is found, each with the date it was read. |
| market data sources | read | The rounds, hires, sales and ownership changes that are the signs a company may be ready. |
| the research library | read | The evidence the thesis was tested against, kept by the researcher agent. |
| the restricted list | read | A company on it is never approached. |
| the email system | write | The one follow-up sent on its date. |
| the notification channel | write | A sign reaches the owning partner within the days the policy sets. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
