# The systems this abstract agent needs

Thirteen systems, named by role rather than by product. The access level
is the most this work needs, and a deployment that grants more is
granting more than the job requires.

| Role | Access | What the access is for |
|---|---|---|
| analytics platforms | read |  |
| ad platforms | read |  |
| the CRM | read |  |
| the HR system | read | The people employed at each period end by team, level and location, the hires, leavers and internal moves, and the reasons leavers gave counted by category, with no protected characteristic and no leaver's own words. |
| the applicant tracking system | read | The time to fill each position closed in the period. |
| the payroll system | read | The people paid in the period and the cost of pay, benefits and the employer's taxes on pay, totaled by team. |
| the ledger | read | The labor cost as the books carry it, which the HR system's and the payroll system's figures are compared against. |
| the support system | read | Each case with its queue, channel, topic, plan, clock stamps and the articles it cites, with no right to change a case. |
| the phone system | read | The calls that arrived in each interval and how long each was handled. |
| the chat tool | read | The chats that arrived in each interval and how long each was handled. |
| the knowledge base | read | The articles live in the help center at their versions. |
| the help center's search and reading record | read | What customers searched for and read, with any personal data removed. |
| the complaints register | read | The formal complaints by class, outcome and time to answer. |

Whoever builds an agent from this plugin writes the `mcp.json` that
points these roles at their own systems. Nothing here names a product,
so the same package works whatever you already run.
